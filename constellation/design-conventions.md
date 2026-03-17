# TrendLife — Kaleidoscope Icon Conventions

> 完整設計系統（色彩、字型、元件、動畫）請見 `style.md`。
> 本文件只記錄 Kaleidoscope icon 的規範，這些規範 **override VD 原稿的 inline SVG 做法**。

---

## Asset

- **File:** `kaleidoscope-mandala.svg`
- **Location:** `constellation/kaleidoscope-mandala.svg`
- 永遠使用此 SVG 檔案，不得替換為 inline SVG path、emoji 或其他 AI icon。

---

## 使用情境尺寸

| Context | Size | Class / Treatment |
|---|---|---|
| Bottom nav center button | 22 × 22 px | `<img class="nav-ai-img">` inside `.nav-ai` |
| Chat header avatar | 26 × 26 px inside 40px container | `<img>` inside `.chat-pg-avatar` |
| Chat message avatar | 20 × 20 px inside 30px container | `<img>` inside `.chat-msg-av.ai-av` |
| Chat input send button | 16 × 16 px | `<img>` with `filter: brightness(0) invert(1)` |

---

## Bottom Nav Button HTML

```html
<button class="nav-item nav-ai" id="nav-ai" aria-label="Kaleidoscope AI" onclick="goChat()">
  <!-- Rotating ring (always present, visible only when active) -->
  <svg class="nav-ai__ring" viewBox="0 0 100 100" fill="none">
    <circle cx="50" cy="50" r="46" stroke="rgba(192,132,252,0.6)" stroke-width="1"
      stroke-dasharray="4 3" fill="none">
      <animateTransform attributeName="transform" type="rotate"
        values="0 50 50;360 50 50" dur="12s" repeatCount="indefinite"/>
    </circle>
    <circle cx="50" cy="50" r="46" stroke="rgba(0,188,212,0.4)" stroke-width="0.5" fill="none">
      <animateTransform attributeName="transform" type="rotate"
        values="360 50 50;0 50 50" dur="15s" repeatCount="indefinite"/>
    </circle>
  </svg>
  <!-- Orbiting particles -->
  <div class="nav-ai__orbit"></div>
  <!-- Kaleidoscope icon -->
  <img class="nav-ai-img" src="kaleidoscope-mandala.svg" alt="Kaleidoscope">
</button>
```

---

## Icon 顏色規則

| State | Treatment |
|---|---|
| Inactive | `opacity: 0.85`，自然色 |
| Active | `opacity: 1; filter: brightness(0) invert(1)` — 白色，顯示於紫色底 |
| Chat avatar | 自然色（無 filter），20×20px，teal 容器 `rgba(0,188,212,0.1)` + `border: 1px solid rgba(0,188,212,0.25)` |

---

## Button Active 動畫

- Breathing radial glow（3.2s pulse）
- Dual counter-rotating rings：紫 `rgba(192,132,252,0.6)` 12s + 青 `rgba(0,188,212,0.4)` 15s
- Orbiting dot particles（8s spin）
- Icon float up/down 1.5px（4s ease）
