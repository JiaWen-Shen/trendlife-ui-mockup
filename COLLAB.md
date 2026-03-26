# TrendLife Mockup — 協作計劃

## 成員與分工

| 角色 | 代稱 | 負責範圍 |
|-----|------|---------|
| 專案負責人（Owner） | Karen | 整體方向、story.md、CLAUDE.md、Vercel 部署、demo-scripts/ |
| Visual Designer | [VD] | constellation/ 所有設計檔案 |

---

## 檔案分工

### Owner 主責
- `CLAUDE.md` — 工作指示（改動前先討論）
- `story.md` — 產品故事線
- `design-conventions.md` — 設計規範（可提案，Owner 審核後更新）
- `demo-scripts/` — Demo 錄製腳本
- `reference/` — 視覺參考資料

### [VD] 主責
- `constellation/mockup-mei-v2.html`
- `constellation/mockup-yuki-ipad.html`
- `constellation/style.md` — 設計系統（可直接修改）
- `constellation/design-conventions.md` — Kaleidoscope icon 規範（可直接修改）
- `constellation/kaleidoscope-mandala.svg` / `bloom-icon.svg`

### 共用
- `vd-collab/` — VD 原稿 prototype 參考
- `README.md`

---

## Branch 策略

```
main
 └── vd/<任務名稱>    ← [VD] 的工作 branch
```

### [VD] 工作流程
1. 開新 branch：`vd/<任務>`（例如：`vd/yuki-growth-report`）
2. 在 Claude Code 裡開工，說：「我要改 `<檔案>`，branch 是 `vd/<任務>`，先 pull 最新」
3. 修改完成，確認 preview 沒問題後說：「好，可以 commit」
4. Claude 自動 commit → push → 開 PR 給 Karen review
5. Karen 在 GitHub 上 review → merge

### Owner 工作流程
- 可直接在 `main` 修改非設計內容（story.md、CLAUDE.md 等）
- 設計改動也開 feature branch，避免直接改 main 上的 HTML

---

## Commit 規範

格式：`design: <改動摘要>`（中文 OK）

範例：
- `design: Yuki 成長報告新增 AI 使用圓餅圖`
- `design: 修正 BP Alert banner 捲動速度`
- `design: 更新 style.md accent color token`

---

## 部署規則

- **只有 Owner 可以部署**
- 指令：`cd constellation && npx vercel --prod --yes`
- 說「請部署」才觸發，[VD] 的修改 merge 進 main 後由 Karen 決定何時部署
- 現有固定 URL：
  - Mayumi 視角：https://trendlife-constellation.vercel.app/mockup-mei-v2.html
  - Yuki 視角：https://trendlife-constellation.vercel.app/mockup-yuki-ipad.html

---

## 設計規範文件（Claude 自動載入）

每次在這個 repo 啟動 Claude，以下三份文件會自動成為 context：

| 文件 | 內容 |
|-----|------|
| `design-conventions.md` | 圖表模式、互動狀態、icon 規範 |
| `constellation/style.md` | 色彩 token、字型、間距、元件 |
| `constellation/design-conventions.md` | Kaleidoscope icon 專屬規則 |

**不需要每次提醒 Claude 遵守規範，它會自動參照。**

---

## 衝突處理

- 同一個檔案不要同時修改（改之前先 pull，確認沒有 in-progress PR）
- 有疑問先在 PR comment 留言，不要直接 force push
- 設計方向有分歧 → 截圖 + 說明，讓 Karen 決定

---

## 實作摘要（簡報素材）

### 核心機制

兩位協作者（Karen + VD）各自使用 Claude Code，但共用同一份 repo 裡的 context 文件。**Claude Code 啟動時會自動載入這些文件**，不需要手動設定，確保兩個 Claude 的行為一致。

### 自動載入的 Context（pull repo 即生效）

```
CLAUDE.md              ← Claude Code 的工作指示（主入口）
  @story.md            ← 產品故事線，設計決策的依據
  @design-conventions.md         ← 圖表規範、互動狀態、icon 規則
  @constellation/style.md        ← 色彩 token、字型、元件樣式
  @constellation/design-conventions.md  ← Kaleidoscope icon 專屬規則
```

VD `git clone` 後直接執行 `claude`，以上全部自動生效。

### 角色識別

CLAUDE.md 裡設定了 branch 判斷邏輯：

| Branch | 身份 | Claude 行為 |
|--------|------|------------|
| `vd/xxx` | VD | commit 後自動開 PR，不可部署 |
| `main` / 其他 | Karen | 可直接 push，可部署 Vercel |

### VD 工作流程

```
1. git checkout -b vd/<任務名稱>
2. 執行 claude，說明今天要改什麼
3. Claude 修改 → 本機 preview → 確認
4. 說「好，可以 commit」
5. Claude 自動 commit → push → 開 PR
6. Karen review → merge → 決定是否部署
```

### 文件清單

| 文件 | 對象 | 用途 |
|-----|------|------|
| `CLAUDE.md` | Claude | 工作指示、角色識別、部署規則 |
| `COLLAB.md` | 人 | 分工、branch 策略、衝突處理 |
| `VD_GUIDE.md` | VD | Claude Code 操作指南、常用句型 |
| `story.md` | Claude | 產品故事線（設計背景 context） |
| `constellation/style.md` | Claude | 設計系統 |
