#!/usr/bin/env python3
"""Push captured HTML to Figma via Remote MCP generate_figma_design.

Usage:
  python3 figma-mcp-push.py [--file FILE_KEY] [--new FILE_NAME]

Flow:
  1. Read _figma-push.json manifest (component name + URL)
  2. Authenticate with Figma Remote MCP (OAuth 2.0 + PKCE)
  3. Call generate_figma_design → get captureId
  4. POST captureId to bridge server → browser loads capture iframe
  5. Poll generate_figma_design until capture completes
"""
import argparse, base64, hashlib, http.server, json, os, secrets, sys, threading, time, urllib.parse, urllib.request, webbrowser

DIR = os.path.dirname(os.path.abspath(__file__))
TOKEN_PATH = '/tmp/figma_oauth_token.json'
STATE_PATH = '/tmp/figma_oauth_state.json'
MCP_URL = 'https://mcp.figma.com/mcp'
BRIDGE = 'http://localhost:8321'
CALLBACK_PORT = 9274

session_id = None

# ── OAuth 2.0 + PKCE ──

def load_token():
    if os.path.exists(TOKEN_PATH):
        with open(TOKEN_PATH) as f:
            return json.load(f)
    return None

def save_token(token_data):
    with open(TOKEN_PATH, 'w') as f:
        json.dump(token_data, f, indent=2)

def register_client():
    data = json.dumps({
        "client_name": "Claude Code MCP Client",
        "redirect_uris": [f"http://127.0.0.1:{CALLBACK_PORT}/callback"],
        "grant_types": ["authorization_code", "refresh_token"],
        "response_types": ["code"],
        "token_endpoint_auth_method": "none",
        "scope": "mcp:connect"
    }).encode()
    req = urllib.request.Request(
        "https://api.figma.com/v1/oauth/mcp/register",
        data=data,
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req)
    return json.loads(resp.read())

def do_oauth():
    print("[OAuth] Registering client…")
    client = register_client()
    client_id = client['client_id']
    client_secret = client.get('client_secret', '')

    code_verifier = secrets.token_urlsafe(64)
    code_challenge = base64.urlsafe_b64encode(
        hashlib.sha256(code_verifier.encode()).digest()
    ).rstrip(b'=').decode()
    state = secrets.token_urlsafe(32)

    # Save state for verification
    with open(STATE_PATH, 'w') as f:
        json.dump({
            'client_id': client_id,
            'client_secret': client_secret,
            'code_verifier': code_verifier,
            'state': state
        }, f)

    auth_code = [None]
    server_done = threading.Event()

    class CallbackHandler(http.server.BaseHTTPRequestHandler):
        def do_GET(self):
            qs = urllib.parse.parse_qs(urllib.parse.urlparse(self.path).query)
            if qs.get('state', [None])[0] == state and 'code' in qs:
                auth_code[0] = qs['code'][0]
                self.send_response(200)
                self.send_header('Content-Type', 'text/html')
                self.end_headers()
                self.wfile.write(b'<h2>Authorized! You can close this tab.</h2>')
                server_done.set()
            else:
                self.send_response(400)
                self.end_headers()
                self.wfile.write(b'Authorization failed')
        def log_message(self, *a): pass

    srv = http.server.HTTPServer(('127.0.0.1', CALLBACK_PORT), CallbackHandler)
    t = threading.Thread(target=srv.serve_forever, daemon=True)
    t.start()

    auth_url = (
        f"https://www.figma.com/oauth/mcp?"
        f"client_id={client_id}&"
        f"redirect_uri=http%3A%2F%2F127.0.0.1%3A{CALLBACK_PORT}%2Fcallback&"
        f"response_type=code&scope=mcp%3Aconnect&"
        f"state={state}&"
        f"code_challenge={code_challenge}&"
        f"code_challenge_method=S256"
    )
    print(f"[OAuth] Opening browser for authorization…")
    webbrowser.open(auth_url)
    print(f"[OAuth] Waiting for callback on port {CALLBACK_PORT}…")

    server_done.wait(timeout=120)
    srv.shutdown()

    if not auth_code[0]:
        print("[OAuth] ERROR: No authorization code received")
        sys.exit(1)

    print("[OAuth] Exchanging code for token…")
    token_data = urllib.parse.urlencode({
        'client_id': client_id,
        'client_secret': client_secret,
        'code': auth_code[0],
        'redirect_uri': f'http://127.0.0.1:{CALLBACK_PORT}/callback',
        'grant_type': 'authorization_code',
        'code_verifier': code_verifier
    }).encode()
    req = urllib.request.Request(
        "https://api.figma.com/v1/oauth/token",
        data=token_data,
        headers={"Content-Type": "application/x-www-form-urlencoded"}
    )
    resp = urllib.request.urlopen(req)
    token = json.loads(resp.read())
    save_token(token)
    print(f"[OAuth] Token saved (expires_in: {token.get('expires_in', '?')}s)")
    return token

# ── MCP JSON-RPC ──

def mcp_call(method, params=None, msg_id=1, token=None):
    global session_id
    payload = {"jsonrpc": "2.0", "id": msg_id, "method": method}
    if params:
        payload["params"] = params
    data = json.dumps(payload).encode()
    headers = {
        "Content-Type": "application/json",
        "Accept": "application/json, text/event-stream"
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if session_id:
        headers["mcp-session-id"] = session_id
    req = urllib.request.Request(MCP_URL, data=data, headers=headers)
    resp = urllib.request.urlopen(req)
    sid = resp.headers.get("mcp-session-id")
    if sid:
        session_id = sid
    raw = resp.read().decode()
    # Parse SSE format
    for line in raw.split("\n"):
        if line.startswith("data: "):
            return json.loads(line[6:])
    # Try direct JSON
    try:
        return json.loads(raw)
    except:
        return {"raw": raw}

def mcp_notify(method, token=None):
    global session_id
    payload = {"jsonrpc": "2.0", "method": method}
    data = json.dumps(payload).encode()
    headers = {"Content-Type": "application/json"}
    if token:
        headers["Authorization"] = f"Bearer {token}"
    if session_id:
        headers["mcp-session-id"] = session_id
    req = urllib.request.Request(MCP_URL, data=data, headers=headers)
    try:
        urllib.request.urlopen(req)
    except:
        pass

# ── Main flow ──

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--file', help='Existing Figma file key to push into')
    parser.add_argument('--new', help='Create new Figma file with this name')
    parser.add_argument('--plan-key', help='Figma org/team planKey', default='organization::854756275776512450')
    args = parser.parse_args()

    # 1. Read manifest
    manifest_path = os.path.join(DIR, '_figma-push.json')
    if not os.path.exists(manifest_path):
        print("ERROR: No _figma-push.json found. Click 'Push to Figma' in the prototype first.")
        sys.exit(1)
    with open(manifest_path) as f:
        manifest = json.load(f)
    component = manifest.get('component', 'component')
    capture_url = manifest.get('url', '')
    print(f"[Push] Component: {component}")
    print(f"[Push] Capture URL: {capture_url}")

    # 2. Get OAuth token
    token_data = load_token()
    if not token_data or 'access_token' not in token_data:
        token_data = do_oauth()
    access_token = token_data['access_token']

    # 3. Initialize MCP session
    print("[MCP] Initializing session…")
    init_resp = mcp_call("initialize", {
        "protocolVersion": "2025-03-26",
        "capabilities": {},
        "clientInfo": {"name": "claude-code", "version": "1.0.0"}
    }, msg_id=1, token=access_token)
    print(f"[MCP] Session: {session_id}")

    mcp_notify("notifications/initialized", token=access_token)

    # 4. Call generate_figma_design
    print("[MCP] Calling generate_figma_design…")
    gen_args = {}
    if args.file:
        gen_args["outputMode"] = "existingFile"
        gen_args["fileKey"] = args.file
    elif args.new:
        gen_args["outputMode"] = "newFile"
        gen_args["fileName"] = args.new
        gen_args["planKey"] = args.plan_key
    else:
        gen_args["outputMode"] = "newFile"
        gen_args["fileName"] = f"TrendLife — {component}"
        gen_args["planKey"] = args.plan_key

    gen_resp = mcp_call("tools/call", {
        "name": "generate_figma_design",
        "arguments": gen_args
    }, msg_id=2, token=access_token)
    print(f"[MCP] Response: {json.dumps(gen_resp, indent=2)[:500]}")

    # Extract captureId from response
    capture_id = None
    if 'result' in gen_resp:
        result = gen_resp['result']
        if isinstance(result, dict):
            # Look in content array
            for item in result.get('content', []):
                text = item.get('text', '')
                if 'captureId' in text:
                    # Try to parse as JSON
                    try:
                        d = json.loads(text)
                        capture_id = d.get('captureId')
                    except:
                        pass
                if not capture_id and 'capture' in text.lower():
                    # Try to find captureId in text
                    import re
                    m = re.search(r'[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{12}', text)
                    if m:
                        capture_id = m.group(0)

    if not capture_id:
        print(f"[MCP] ERROR: Could not extract captureId from response")
        print(f"[MCP] Full response: {json.dumps(gen_resp, indent=2)}")
        sys.exit(1)

    print(f"[MCP] captureId: {capture_id}")

    # 5. POST captureId to bridge
    print("[Bridge] Sending captureId to bridge…")
    bridge_data = json.dumps({"captureId": capture_id}).encode()
    req = urllib.request.Request(
        f"{BRIDGE}/api/figma-capture-id",
        data=bridge_data,
        headers={"Content-Type": "application/json"}
    )
    resp = urllib.request.urlopen(req)
    print(f"[Bridge] {resp.read().decode()}")

    # 6. Wait for capture.js to finish (browser will load the iframe)
    print("[Capture] Waiting for browser to capture DOM…")
    time.sleep(15)

    # 7. Poll generate_figma_design for completion
    print("[MCP] Polling for completion…")
    for i in range(12):
        poll_resp = mcp_call("tools/call", {
            "name": "generate_figma_design",
            "arguments": {"captureId": capture_id}
        }, msg_id=3+i, token=access_token)
        print(f"[MCP] Poll {i+1}: {json.dumps(poll_resp, indent=2)[:300]}")

        if 'result' in poll_resp:
            result = poll_resp['result']
            for item in result.get('content', []):
                text = item.get('text', '')
                if 'completed' in text.lower() or 'success' in text.lower():
                    print(f"\n✓ Component '{component}' pushed to Figma!")
                    return
        time.sleep(5)

    print("[MCP] Capture may still be processing. Check Figma.")

if __name__ == '__main__':
    main()
