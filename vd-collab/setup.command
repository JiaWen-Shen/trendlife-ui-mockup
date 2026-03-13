#!/bin/bash
# VD Collaboration Setup — run this ONCE the first time
# Double-click this file in Finder to run

# Auto-cd to repo root (so double-click from Finder works)
SCRIPT_DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" && pwd )"
REPO_DIR="$(dirname "$SCRIPT_DIR")"
REPO_URL="https://github.com/karen-shen_tmemu/trendlife-ui-mockup.git"
DESKTOP_DIR="$HOME/Desktop/trendlife-ui-mockup"

clear
echo ""
echo "  🎨  Trendlife UI Mockup — 協作環境設定"
echo "  ========================================="
echo ""

# ── 1. Check git ──────────────────────────────────────────────────────────────
if ! command -v git &> /dev/null; then
  echo "  ❌  找不到 git，請先在終端機執行以下指令後重新開啟："
  echo "      xcode-select --install"
  echo ""
  read -n1 -r -p "  按任意鍵關閉..." _
  exit 1
fi

# ── 2. Configure git identity ─────────────────────────────────────────────────
if [ -z "$(git config --global user.name)" ]; then
  echo "  第一次設定，請輸入你的名字（會出現在版本記錄）："
  read -rp "  名字 > " GIT_NAME
  git config --global user.name "$GIT_NAME"
fi

if [ -z "$(git config --global user.email)" ]; then
  echo "  請輸入你的 GitHub 信箱："
  read -rp "  Email > " GIT_EMAIL
  git config --global user.email "$GIT_EMAIL"
fi

# ── 3. Clone or update repo ───────────────────────────────────────────────────
if [ -d "$DESKTOP_DIR/.git" ]; then
  echo "  📂  找到現有專案資料夾，更新中..."
  cd "$DESKTOP_DIR"
  git fetch origin --quiet
  echo "  ✓  更新完成"
else
  echo "  📥  下載專案中（第一次需要一點時間）..."
  git clone "$REPO_URL" "$DESKTOP_DIR"
  cd "$DESKTOP_DIR"
  echo "  ✓  下載完成"
fi

cd "$DESKTOP_DIR"

# ── 4. Choose view ────────────────────────────────────────────────────────────
echo ""
echo "  你要修改哪個畫面？"
echo ""
echo "    1)  Mei's view  （父母端 — mockup-eva-view.html）"
echo "    2)  Yuki's view （孩子端 — mockup-yuki-view.html）"
echo ""
read -rp "  請輸入 1 或 2：" VIEW_CHOICE

case "$VIEW_CHOICE" in
  1)
    BRANCH="vd/mei-view-refinement"
    TARGET_FILE="constellation/mockup-eva-view.html"
    LABEL="Mei's view（父母端）"
    ;;
  2)
    BRANCH="vd/yuki-view-refinement"
    TARGET_FILE="constellation/mockup-yuki-view.html"
    LABEL="Yuki's view（孩子端）"
    ;;
  *)
    echo ""
    echo "  ❌  無效的選擇，請重新執行 setup.command"
    read -n1 -r -p "  按任意鍵關閉..." _
    exit 1
    ;;
esac

# ── 5. Switch branch ──────────────────────────────────────────────────────────
git checkout "$BRANCH" --quiet
git pull origin "$BRANCH" --quiet
echo ""
echo "  ✅  已切換到：$LABEL"

# ── 6. Open preview in browser ────────────────────────────────────────────────
echo "  🌐  在瀏覽器開啟預覽..."
open "$DESKTOP_DIR/$TARGET_FILE"

# ── 7. Open folder in Finder ──────────────────────────────────────────────────
open "$DESKTOP_DIR/constellation"

# ── 8. Summary ────────────────────────────────────────────────────────────────
echo ""
echo "  =================================="
echo "  📁  工作資料夾已在 Finder 開啟"
echo ""
echo "  ✏️   修改這個檔案："
echo "      constellation/$TARGET_FILE"
echo ""
echo "  🚀  改完之後，雙擊執行："
echo "      vd-collab/submit.command"
echo "  =================================="
echo ""
read -n1 -r -p "  按任意鍵關閉視窗..." _
