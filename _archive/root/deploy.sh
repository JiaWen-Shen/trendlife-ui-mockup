#!/bin/bash
set -e

echo "📦 Generating standalone HTML..."
python3 - << 'PYEOF'
import base64, re

base = '/Users/karen_shen/Jottacloud/trendlife-ui-mockup/'
images = {}
for fname, mime in [('reference/logo-full-transparent.png', 'image/png'),
                    ('reference/logo-mark-only.png', 'image/png')]:
    with open(base + fname, 'rb') as f:
        b64 = base64.b64encode(f.read()).decode()
    images[fname] = f'data:{mime};base64,{b64}'

with open(base + 'mockup-scene1.html', 'r') as f:
    html = f.read()

for path, uri in images.items():
    html = html.replace(f'src="{path}"', f'src="{uri}"')

with open(base + 'mockup-scene1-standalone.html', 'w') as f:
    f.write(html)
print("  ✓ mockup-scene1-standalone.html updated")
PYEOF

echo "📤 Committing and pushing to GitHub..."
git add mockup-scene1.html mockup-scene1-standalone.html index.html \
        constellation-spec.html mockup-constellation-draft.html mockup-eva-view.html \
        mockup-yuki-view.html
git diff --staged --quiet || git commit -m "update mockup"
git push

echo "🚀 Deploying to Vercel..."
vercel --prod --yes

echo "✅ Done! https://trendlife-ui-mockup.vercel.app"
