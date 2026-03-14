#!/bin/bash
set -e

DIR="$(cd "$(dirname "$0")" && pwd)"
APP="$DIR/dist/TrendLife Prototype.app"

echo "Building TrendLife Prototype.app..."

# Clean
rm -rf "$APP"

# Create .app bundle structure
mkdir -p "$APP/Contents/MacOS"
mkdir -p "$APP/Contents/Resources/web/faces"

# Compile Swift → binary
swiftc "$DIR/build-app.swift" \
  -o "$APP/Contents/MacOS/TrendLife" \
  -framework Cocoa \
  -framework WebKit \
  -target arm64-apple-macos13.0

# Copy web assets
cp "$DIR/constellation/trendlife-modern.html" "$APP/Contents/Resources/web/"
cp "$DIR/constellation/faces/"*.png "$APP/Contents/Resources/web/faces/" 2>/dev/null || true

# Create Info.plist
cat > "$APP/Contents/Info.plist" << 'PLIST'
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN" "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
    <key>CFBundleName</key>
    <string>TrendLife Prototype</string>
    <key>CFBundleIdentifier</key>
    <string>com.trendmicro.trendlife-prototype</string>
    <key>CFBundleVersion</key>
    <string>1.0.0</string>
    <key>CFBundleShortVersionString</key>
    <string>1.0</string>
    <key>CFBundleExecutable</key>
    <string>TrendLife</string>
    <key>CFBundlePackageType</key>
    <string>APPL</string>
    <key>LSMinimumSystemVersion</key>
    <string>13.0</string>
    <key>NSHighResolutionCapable</key>
    <true/>
    <key>NSSupportsAutomaticGraphicsSwitching</key>
    <true/>
</dict>
</plist>
PLIST

# Size report
SIZE=$(du -sh "$APP" | cut -f1)
echo "Done → $APP ($SIZE)"
