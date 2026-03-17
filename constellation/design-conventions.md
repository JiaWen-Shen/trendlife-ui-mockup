# TrendLife Constellation — Design Conventions

## Kaleidoscope Icon

### Asset
- **File:** `kaleidoscope-mandala.svg`
- **Location:** `constellation/kaleidoscope-mandala.svg`

### Usage Rules
The Kaleidoscope mandala SVG is the **single canonical icon** for all Kaleidoscope AI representations. Do not substitute with an inline SVG path, emoji, or generic AI icon.

| Context | Size | Class / Treatment |
|---|---|---|
| Bottom nav center button | 22 × 22 px | `<img class="nav-ai-img">` inside `.nav-ai` button |
| Chat header avatar | 26 × 26 px inside 40px container | `<img>` inside `.chat-pg-avatar` |
| Chat message avatar | 20 × 20 px inside 30px container | `<img>` inside `.chat-msg-av.ai-av` |
| Chat input send button | 16 × 16 px | `<img>` with `filter: brightness(0) invert(1)` |

### Bottom Nav Button Anatomy

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

### Color Tokens
- **Background (inactive):** `rgba(192,132,252,0.28)` — translucent accent purple
- **Background (active):** `var(--accent)` → `#C084FC`
- **Active glow:** `box-shadow: 0 0 0 3px rgba(192,132,252,0.25), 0 0 18px rgba(192,132,252,0.2)`
- **Icon (inactive):** `opacity: 0.85`
- **Icon (active):** `opacity: 1; filter: brightness(0) invert(1)` — renders white on purple bg
- **Ring strokes:** purple `rgba(192,132,252,0.6)` + cyan `rgba(0,188,212,0.4)`

### Animation States
- **Inactive:** Button sits with gentle translucent purple bg; icon at 85% opacity
- **Active (nav-ai.active):**
  - Breathing radial glow behind button (3.2s pulse)
  - Dual counter-rotating rings (12s / 15s)
  - Orbiting dot particles on the orbit ring
  - Icon floats up/down 1.5px (4s ease)

### Chat Avatar Treatment
When used as an AI message avatar in chat, the icon is displayed inside a teal-tinted container:
```css
background: rgba(0,188,212,0.1);
border: 1px solid rgba(0,188,212,0.25);
```
Icon is rendered at natural color (no filter) at 20×20px.

---

## Color System

| Token | Dark | Light | Usage |
|---|---|---|---|
| `--accent` | `#C084FC` | — | Yuki brand / primary purple |
| `--ai` | `#22D3EE` | — | Kaleidoscope AI / cyan |
| `--violet` | `#8B5CF6` | — | Secondary purple |
| `--bg` | `#09090B` | `#E7EBF0` | Page background |
| `--surface` | `#18181B` | `#FFFFFF` | Card background |

## Typography

- **Font:** `DM Sans` (variable, opsz 9–40)
- **Weights used:** 300 (light), 400 (regular), 500 (medium), 600 (semibold), 700 (bold), 800 (extrabold)

## Layout: iPad Pro 11" Landscape

- **Device viewport:** 1194 × 834px
- **Two-column pattern:** Fixed left pane (316–520px) + `flex:1` right pane
- **App header:** Persistent at top, outside `#page-viewport`
- **Bottom nav:** Persistent `position:absolute; bottom:0`, pill-style, frosted glass, outside `#page-viewport`
- **Pages:** `position:absolute; inset:0` inside `#page-viewport`

## Page Navigation

```
Home (page-home) ←→ Detail (page-detail)   [via goDetail() / goHome()]
Home             ←→ Family (page-family)   [via goFamily() / goHomeFromFamily()]
Home             ←→ Chat (page-chat)       [via goChat() / goHome() on back btn]
```
