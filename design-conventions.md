# TrendLife UI Mockup — Design Conventions

## 互動狀態

- **沒有連結的元素不顯示可點選狀態** — 無 onclick 或導頁行為的卡片/按鈕，必須加 `cursor: default`，並移除 hover/active 的視覺回饋（transform、border highlight 等）
- 實作方式：加 `.static` class，覆蓋 hover/active 樣式

## Icons

- 一律使用 **Material Symbols Outlined** font，不使用 emoji 在 UI 上
- 載入方式：`<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Material+Symbols+Outlined:opsz,wght,FILL,GRAD@20,400,0,0" />`
- 使用方式：`<span class="material-symbols-outlined">icon_name</span>`
- 常用 icon 對照：
  | 情境 | Icon name |
  |------|-----------|
  | 瀏覽數 | `visibility` |
  | 按讚 | `favorite` |
  | 留言 | `chat_bubble` |
  | 趨勢 | `trending_up` |
  | 加入成員 | `group_add` |
  | AI / Kaleidoscope | `auto_awesome` |
  | 已發布 | `check_circle` |
  | WIP | `edit_note` |
  | 通知 | `notifications` |
