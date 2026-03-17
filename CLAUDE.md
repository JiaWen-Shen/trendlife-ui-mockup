# TrendLife UI Mockup — Claude Code 工作指示

這個 repo 是 TrendLife Kaleidoscope 的 UI mockup 專案。

## Git 工作規則

- 修改完成後，只 `git add` 你實際改動的檔案，不用 `git add .`
- Commit message 格式：`design: <改動摘要>`
- Commit 後自動 push 到目前的 branch
- Push 完後，用 `gh pr create --base main --fill` 自動開 PR，不需要用戶額外操作
- **不要 deploy 到 Vercel，除非用戶明確說「請部署」**

## UI 設計規則

- **Icons 一律使用 Material Design 圖示**（Material Symbols Outlined font），不使用 emoji 在 UI 上
- **每次修改完成後，自動在瀏覽器開啟修改的頁面**

## 溝通

- 用中文回應
- 修改前先確認你理解用戶的意圖
- 不確定的地方直接問，不要自己猜
