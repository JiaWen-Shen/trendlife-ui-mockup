# TrendLife UI Mockup — Claude Code 工作指示

這個 repo 是 TrendLife Kaleidoscope 的 UI mockup 專案。
協作規則詳見 `COLLAB.md`。

## 協作成員識別

根據目前所在 branch 判斷用戶身份：
- Branch 開頭為 `vd/` → 用戶是 **[VD]**（Visual Designer）
- 其他 branch（`main`、`feature/` 等）→ 用戶是 **Karen**（Owner）

## Git 工作規則

- 修改完成後，只 `git add` 你實際改動的檔案，不用 `git add .`
- Commit message 格式：`design: <改動摘要>`
- **用戶說「好」或「可以」後才 commit & push**；未確認前只做本機修改
- Commit 後自動 push 到目前的 branch

### [VD] 專屬規則（branch 開頭為 `vd/` 時）
- Push 完成後，**自動開 PR 到 main**：`gh pr create --base main --title "design: <摘要>" --body "改動說明"`
- **不可部署到 Vercel**，部署由 Karen 執行
- 不可直接修改 `CLAUDE.md`、`story.md`、`demo-scripts/`

## 部署規則

- 部署指令：`cd constellation && npx vercel --prod --yes`
- **不要 deploy 到 Vercel，除非用戶明確說「請部署」**
- 固定 URL，不建新 Vercel 專案：
  - Mayumi 視角：https://trendlife-constellation.vercel.app/mockup-mei-v2.html
  - Yuki 視角（iPad，主工作檔）：https://trendlife-constellation.vercel.app/mockup-yuki-ipad.html
  - Yuki 視角（獨立）：https://trendlife-yuki-view.vercel.app
  - Spec：https://trendlife-constellation.vercel.app

## UI 設計規則

@design-conventions.md
@constellation/style.md
@constellation/design-conventions.md

## 工作流程

- **每次修改完成後，自動在瀏覽器開啟修改的頁面**
- 用戶說「請提出設計規劃」時，先討論方向，等用戶確認再執行

## 溝通

- 用中文回應
- 修改前先確認你理解用戶的意圖
- 不確定的地方直接問，不要自己猜
