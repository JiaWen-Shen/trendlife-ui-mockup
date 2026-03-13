#!/bin/bash
# VD Collaboration Submit — run this every time you finish editing
# Double-click this file in Finder to run

DESKTOP_DIR="$HOME/Desktop/trendlife-ui-mockup"

clear
echo ""
echo "  🚀  Trendlife UI Mockup — 送出修改"
echo "  ====================================="
echo ""

# ── 1. Verify repo exists ─────────────────────────────────────────────────────
if [ ! -d "$DESKTOP_DIR/.git" ]; then
  echo "  ❌  找不到專案資料夾"
  echo "      請先雙擊執行 setup.command"
  echo ""
  read -n1 -r -p "  按任意鍵關閉..." _
  exit 1
fi

cd "$DESKTOP_DIR"

# ── 2. Verify on a VD branch ─────────────────────────────────────────────────
CURRENT_BRANCH=$(git branch --show-current)

if [[ "$CURRENT_BRANCH" != vd/* ]]; then
  echo "  ❌  目前不在 VD 工作分支"
  echo "      目前分支：$CURRENT_BRANCH"
  echo "      請先雙擊執行 setup.command 選擇要修改的畫面"
  echo ""
  read -n1 -r -p "  按任意鍵關閉..." _
  exit 1
fi

# ── 3. Determine view label ───────────────────────────────────────────────────
if [[ "$CURRENT_BRANCH" == *"mei"* ]]; then
  VIEW_NAME="Mei's view（父母端）"
  TARGET_FILE="constellation/mockup-eva-view.html"
  PR_URL="https://github.com/karen-shen_tmemu/trendlife-ui-mockup/compare/4-tabs...vd/mei-view-refinement?expand=1"
else
  VIEW_NAME="Yuki's view（孩子端）"
  TARGET_FILE="constellation/mockup-yuki-view.html"
  PR_URL="https://github.com/karen-shen_tmemu/trendlife-ui-mockup/compare/4-tabs...vd/yuki-view-refinement?expand=1"
fi

echo "  📌  目前修改：$VIEW_NAME"
echo "  📌  分支：$CURRENT_BRANCH"
echo ""

# ── 4. Check for changes ──────────────────────────────────────────────────────
CHANGED_FILES=$(git diff --name-only && git diff --staged --name-only)

if [ -z "$CHANGED_FILES" ]; then
  echo "  ⚠️   沒有發現任何修改"
  echo "      請先編輯 HTML 檔案後再執行 submit.command"
  echo ""
  read -n1 -r -p "  按任意鍵關閉..." _
  exit 0
fi

echo "  📝  修改的檔案："
git diff --name-only | while read -r f; do echo "      · $f"; done
echo ""

# ── 5. Ask for description ────────────────────────────────────────────────────
echo "  這次改了什麼？（請簡短描述，中文可以）"
read -rp "  > " COMMIT_MSG

if [ -z "$COMMIT_MSG" ]; then
  COMMIT_MSG="VD refinement update"
fi

echo ""
echo "  📤  送出中..."

# ── 6. Stage only constellation HTML files ────────────────────────────────────
git add constellation/mockup-eva-view.html \
        constellation/mockup-yuki-view.html \
        constellation/constellation-spec.html \
        constellation/*.svg \
        constellation/*.css \
        2>/dev/null || true

# Stage any other tracked changes (won't pick up new untracked files)
git diff --name-only | xargs -I{} git add "{}" 2>/dev/null || true

# ── 7. Commit ─────────────────────────────────────────────────────────────────
git commit -m "$COMMIT_MSG" || {
  echo ""
  echo "  ⚠️   沒有可以送出的修改（可能已送出過）"
  echo ""
  read -n1 -r -p "  按任意鍵關閉..." _
  exit 0
}

# ── 8. Push ───────────────────────────────────────────────────────────────────
git push origin "$CURRENT_BRANCH"

# ── 9. Open PR page ───────────────────────────────────────────────────────────
echo ""
echo "  ✅  送出成功！"
echo ""
echo "  🔗  正在開啟 Pull Request 頁面..."
open "$PR_URL"

echo ""
echo "  ======================================="
echo "  在瀏覽器按下「Create pull request」按鈕"
echo "  Karen 收到通知後會 review 並合併 ✓"
echo ""
echo "  如果要繼續修改另一個 view："
echo "  → 雙擊執行 setup.command，選擇另一個畫面"
echo "  ======================================="
echo ""
read -n1 -r -p "  按任意鍵關閉視窗..." _
