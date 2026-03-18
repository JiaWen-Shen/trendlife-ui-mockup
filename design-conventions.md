# TrendLife UI Mockup — Design Conventions

## 資料呈現：圖表優先，減少文字

**原則：凡是有數量、比例、趨勢的資訊，優先用圖表呈現，不用純文字列舉。**

- **Donut chart** — 用於分類佔比（如防護紀錄的威脅分類、AI 與用戶貢獻比例）
- **Bar / progress bar** — 用於單一指標的進度或強度（如技能成長、螢幕使用時間）
- **Sparkline / trend line** — 用於時間序列趨勢（如週健康數據、活動量變化）
- 圖表旁放圖例和關鍵數字，取代段落說明文字
- 詳細資料用「可展開列表」隱藏，讓 UI 保持乾淨；使用者有需要才展開查看
- 文字說明只保留無法圖像化的質性描述（如 AI 的觀察、建議）

### 實作模式（Donut Chart）

```html
<div class="protection-chart-card">        <!-- flex: donut + legend -->
  <div class="donut-wrap">                 <!-- 86×86px, position:relative -->
    <svg viewBox="0 0 100 100" class="donut-svg">  <!-- rotate(-90deg) via CSS -->
      <circle cx="50" cy="50" r="38" fill="none" stroke="var(--surface2)" stroke-width="15"/>
      <!-- segment: stroke-dasharray="佔比px 238.76", stroke-dashoffset="-累計前段px" -->
    </svg>
    <div class="donut-center"><div class="donut-num">總數</div><div class="donut-sub">blocked</div></div>
  </div>
  <div class="donut-legend">              <!-- 圖例：色點 + 數值 + 類別名 -->
    <div class="donut-leg-item">...</div>
  </div>
</div>
```

CSS classes: `.protection-chart-card`, `.donut-wrap`, `.donut-svg`, `.donut-center`, `.donut-num`, `.donut-sub`, `.donut-legend`, `.donut-leg-item`, `.donut-leg-dot`, `.donut-leg-val`, `.donut-leg-lbl`（已定義於 mockup-mei-v2.html）

---

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
