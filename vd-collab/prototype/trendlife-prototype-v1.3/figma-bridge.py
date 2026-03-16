#!/usr/bin/env python3
"""Bridge server: serves prototype + orchestrates Figma MCP capture flow.

Endpoints:
  POST /api/figma-push        — save component HTML (with capture.js injected)
  POST /api/figma-capture-id  — Claude sets captureId after calling MCP
  GET  /api/figma-status      — browser polls for captureId + status
"""
import http.server, json, os, time

DIR = os.path.dirname(os.path.abspath(__file__))

CAPTURE_SCRIPT = '<script src="https://mcp.figma.com/mcp/html-to-design/capture.js" async></script>'

# In-memory capture state
state = {
    'captureId': None,
    'status': 'idle',
    'component': None,
}

class Handler(http.server.SimpleHTTPRequestHandler):

    def do_GET(self):
        if self.path == '/api/figma-status':
            self._json(200, state)
        else:
            super().do_GET()

    def do_POST(self):
        if self.path == '/api/figma-push':
            try:
                body = self._read_json()
                html = body.get('html', '')
                name = body.get('name', 'component')

                # Inject Figma capture.js into <head>
                if '<head>' in html:
                    html = html.replace('<head>', '<head>\n' + CAPTURE_SCRIPT, 1)
                else:
                    html = '<html><head>' + CAPTURE_SCRIPT + '</head>\n' + html

                filepath = os.path.join(DIR, '_figma-capture.html')
                with open(filepath, 'w', encoding='utf-8') as f:
                    f.write(html)

                manifest = {
                    'component': name,
                    'file': filepath,
                    'url': 'http://localhost:8321/_figma-capture.html',
                    'ts': time.time()
                }
                with open(os.path.join(DIR, '_figma-push.json'), 'w') as f:
                    json.dump(manifest, f, indent=2)

                # Reset state — waiting for Claude to provide captureId
                state['captureId'] = None
                state['status'] = 'waiting'
                state['component'] = name

                self._json(200, {'ok': True, 'url': manifest['url'], 'component': name})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})

        elif self.path == '/api/figma-capture-id':
            try:
                body = self._read_json()
                cid = body.get('captureId', '')
                state['captureId'] = cid
                state['status'] = 'capturing'
                self._json(200, {'ok': True, 'captureId': cid})
            except Exception as e:
                self._json(500, {'ok': False, 'error': str(e)})

        else:
            self.send_error(404)

    def do_OPTIONS(self):
        self.send_response(204)
        self.send_header('Access-Control-Allow-Origin', '*')
        self.send_header('Access-Control-Allow-Methods', 'GET, POST, OPTIONS')
        self.send_header('Access-Control-Allow-Headers', 'Content-Type')
        self.send_header('Content-Length', '0')
        self.end_headers()

    # ── helpers ──

    def _read_json(self):
        length = int(self.headers.get('Content-Length', 0))
        return json.loads(self.rfile.read(length))

    def _json(self, code, data):
        resp = json.dumps(data).encode()
        self.send_response(code)
        self.send_header('Content-Type', 'application/json')
        self.send_header('Content-Length', str(len(resp)))
        self.send_header('Access-Control-Allow-Origin', '*')
        self.end_headers()
        self.wfile.write(resp)

    def log_message(self, fmt, *args):
        pass

if __name__ == '__main__':
    os.chdir(DIR)
    s = http.server.HTTPServer(('', 8321), Handler)
    print('Figma Bridge \u2192 http://localhost:8321')
    print('  POST /api/figma-push        \u2014 save component HTML')
    print('  POST /api/figma-capture-id  \u2014 set captureId from MCP')
    print('  GET  /api/figma-status      \u2014 poll capture status')
    s.serve_forever()
