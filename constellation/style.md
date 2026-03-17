# TrendLife — Design Style Guide

Derived from VD source files:
- `vd-collab/prototype/trendlife-prototype-v1.3/trendlife-modern.html` (Eva/Mei phone view)
- `vd-collab/prototype/yuki-ipad/mockup-yuki-ipad.html` (Yuki iPad view)

For Kaleidoscope icon rules, see `design-conventions.md` (those rules override VD inline SVG).

---

## Color Tokens

### Shared Foundation (all personas)

```css
/* Dark mode (default) */
--bg:       #09090B;   /* page background */
--surface:  #18181B;   /* card background */
--surface2: #27272A;   /* input, secondary surface */
--surface3: #3F3F46;   /* tertiary (dividers, track bg) */

--border:   rgba(255,255,255,0.06);
--border2:  rgba(255,255,255,0.1);

--text:     #FAFAFA;
--text2:    #A1A1AA;
--text3:    #8A8A93;

/* Semantic colors */
--coral:       #F43F5E;   coral-dim: rgba(244,63,94,0.1)
--teal:        #14B8A6;   teal-dim:  rgba(20,184,166,0.08)
--violet:      #8B5CF6;   violet-dim:rgba(139,92,246,0.1)
--sky:         #38BDF8;   sky-dim:   rgba(56,189,248,0.08)
--green:       #22C55E;   green-dim: rgba(34,197,94,0.08)

/* Light mode overrides */
--bg:       #E7EBF0;
--surface:  #FFFFFF;
--surface2: #D8DEE6;
--surface3: #BFC8D2;
--border:   rgba(0,0,0,0.16);
--border2:  rgba(0,0,0,0.25);
--text:     #0F172A;
--text2:    #1E293B;
--text3:    #374151;
```

### Per-Persona Accent (important: do NOT mix)

| Persona | `--accent` | `--accent2` | `--accent-dim` | Usage |
|---|---|---|---|---|
| Eva / Mei (parent) | `#F97316` | `#FB923C` | `rgba(249,115,22,0.1)` | parent/caregiver views |
| Yuki (child) | `#C084FC` | `#D8B4FE` | `rgba(192,132,252,0.06)` | Yuki's creative space |
| Light mode Eva | `#B45309` | `#C2410C` | — | |
| Light mode Yuki | — | — | `rgba(192,132,252,0.12)` | |

### Kaleidoscope AI Color (consistent across all personas)

```css
--ai:     #22D3EE;   /* cyan — all AI-originated elements */
--ai-dim: rgba(0,188,212,0.08);
```

AI orbs, AI chat bubbles, AI notice cards, authorship AI portion → always `--ai` cyan.

---

## Typography

- **Font**: `'DM Sans', system-ui, -apple-system, sans-serif`
- **Import**: `DM Sans` variable, opsz 9–40, weights 300–800
- **Smoothing**: `-webkit-font-smoothing: antialiased`

### Type Scale

| Role | Size | Weight | Letter-spacing | Notes |
|---|---|---|---|---|
| Page title (Home) | 28px | 800 | -0.8px | Phone; gradient text on keyword |
| Section title (Events) | 24px | 800 | -0.6px | |
| Card title | 14px | 700 | -0.2px | |
| Body / message | 13.5px | 400–500 | -0.1px | line-height 1.5 |
| Section label | 12px | 700 | 0.5px | uppercase, color `--text3` |
| Nav label | 10px | 600 | 0.3px | uppercase optional |
| Badge / eyebrow | 9–10px | 700 | 0.3–0.6px | uppercase |
| Timestamp / meta | 10–11px | 400–500 | 0 | color `--text3` |

---

## Spacing & Border Radius

```css
--radius:    20px;   /* cards, primary containers */
--radius-sm: 12px;   /* secondary components */
--radius-xs: 8px;    /* small elements, tooltips */
/* 100px = pill — nav items, tags, input bars */
/* 44px  = device frame phone */
/* 18px  = device frame iPad */
```

Content side padding: `20px` (phone), `24px` (iPad headers).

---

## Easing

```css
--ease-out:    cubic-bezier(0.16, 1, 0.3, 1);    /* primary motion — snappy decel */
--ease-spring: cubic-bezier(0.34, 1.56, 0.64, 1); /* icon/button spring, slight overshoot */
```

Transitions on interactive elements: `0.2–0.25s var(--ease-out)` for most, `0.35–0.4s` for page transitions.

---

## Device Frames

### Phone (375 × 812 px)
```css
border-radius: 44px;
box-shadow: 0 0 0 10px #111, 0 0 0 11px rgba(255,255,255,0.06), 0 30px 100px rgba(0,0,0,0.6);
```

### iPad Pro 11" Landscape (1194 × 834 px)
```css
border-radius: 18px;
box-shadow: 0 0 0 10px #111, 0 0 0 11px rgba(255,255,255,0.06), 0 30px 100px rgba(0,0,0,0.6);
```

---

## Layout System

### Phone Layout
- **Status bar**: 54px, sticky top, frosted glass `rgba(9,9,11,0.5) backdrop-filter:blur(20px) saturate(180%)`
- **Scrollable area**: `padding-top:54px; padding-bottom:96px`
- **Bottom nav**: `position:absolute; bottom:0; padding:0 8px 8px`
- **Bottom fade mask**: 120px gradient `to bottom` at bottom of each view
- Scrollbar: always hidden (`scrollbar-width:none; ::-webkit-scrollbar{display:none}`)

### iPad Layout
- **Status bar**: 24px, surface background, border-bottom
- **App header**: 60px, `background:var(--surface); border-bottom:1px solid var(--border)`
  - Includes: logo + name (left), spacer, search input (260px), icon buttons (44×44px), avatar (40px)
- **App body**: `flex:1; overflow-y:auto`
- **Editor 3-col**: `grid-template-columns: 232px 1fr 312px`
- **Bottom nav**: same pill pattern as phone but higher opacity

---

## Page / View Transition System

### Phone (`.view` system)
```css
.view {
  position: absolute; inset: 0;
  opacity: 0; transform: translateX(20px); pointer-events: none;
  transition: opacity 0.4s var(--ease-out), transform 0.4s var(--ease-out);
}
.view.active   { opacity: 1; transform: translateX(0); pointer-events: auto; }
.view.exit-left{ opacity: 0; transform: translateX(-20px); }
```

### iPad (`.page` system)
```css
.page {
  position: absolute; inset: 0;
  opacity: 0; transform: translateX(40px); pointer-events: none;
  transition: opacity 0.35s var(--ease-out), transform 0.35s var(--ease-out);
}
.page.active   { opacity: 1; transform: translateX(0); pointer-events: auto; }
.page.exit-left{ opacity: 0; transform: translateX(-40px); }
```

**Critical**: always iterate ALL page IDs when switching — never only deactivate one. See `showPage()` pattern in `mockup-yuki-ipad.html`.

---

## Bottom Navigation

Pill-shaped frosted glass bar, `position:absolute; bottom:0`.

```css
.bottom-nav-inner {
  display: flex; align-items: center; justify-content: space-around;
  background: rgba(24,24,27,0.55);          /* phone; iPad uses 0.78 */
  backdrop-filter: blur(24px) saturate(180%);
  border: 1px solid var(--border2);
  border-radius: 100px;
  padding: 8px 6px;
}

.nav-item         { padding: 6px 18px; border-radius: 100px; }
.nav-item.active  { background: var(--accent-dim); }
.nav-icon         { font-size: 20px; }
.nav-item.active .nav-icon  { transform: scale(1.12); }
.nav-label        { font-size: 10px; font-weight: 600; color: var(--text3); }
.nav-item.active .nav-label { color: var(--accent); }
.nav-item:hover:not(.active):not(.nav-ai) { background: rgba(255,255,255,0.04); }
```

Light mode nav: `background:rgba(255,255,255,0.55–0.82)`.

---

## Center AI Button (Kaleidoscope)

```css
.nav-ai {
  width: 52px; height: 52px;         /* phone: 52px, iPad: 48px */
  border-radius: 50%; padding: 0;
  background: rgba(accent, 0.25–0.28); /* per-persona inactive color */
  position: relative; z-index: 10;
}
.nav-ai.active {
  background: var(--accent);
  box-shadow: 0 0 0 3px rgba(accent, 0.25), 0 0 18px rgba(accent, 0.2);
}
```

**Active state effects**:
- Breathing radial glow `::before` (3.2s pulse, blur+fractal warp filter)
- Outer halo `::after` (3.2s, scale 0.9→1.18)
- Dual counter-rotating SVG ring (12s / 15s), `.nav-ai__ring`
- Two orbiting particle dots, `navAiOrbitSpin` 8s linear
- Icon float up/down 1.5px, `navAiFloat` 4s ease-in-out

**⚠️ Icon override** (our rule, not VD): VD uses inline SVG path. We use `kaleidoscope-mandala.svg`:
```html
<img class="nav-ai-img" src="kaleidoscope-mandala.svg" alt="Kaleidoscope">
```
See `design-conventions.md` for full Kaleidoscope icon rules.

---

## Cards

### Base Card Pattern
```css
background: var(--surface);
border: 1px solid var(--border);
border-radius: var(--radius);
```
- Hover: `border-color: var(--border2)`, optional hover glow `::before` radial-gradient
- Active: `transform: scale(0.97)`
- Transition: `0.25s var(--ease-out)` on transform + border-color

### Bento Cards
```css
.bento { display: grid; grid-template-columns: 1fr 1fr; gap: 10px; padding: 0 20px; }
.bento-card { padding: 16px; }
.bento-icon { font-size: 28px; margin-bottom: 10px; }
.bento-title { font-size: 14px; font-weight: 700; }
.bento-desc  { font-size: 11.5px; color: var(--text3); line-height: 1.5; }
/* Corner glow: .bento-card::before — 80px circle, opacity 0.06 */
```

### Project Cards (iPad grid)
```css
.projects-grid { grid-template-columns: repeat(3, 1fr); gap: 16px; }
.proj-thumb { height: 110px; overflow: hidden; }
.proj-type  { font: 500 10px/1; uppercase; letter-spacing .08em; color: var(--text3); }
.proj-title { font: 600 14px/1.3; letter-spacing -0.4px; }
```

---

## Section Headers

### Phone (`section-hdr`)
```css
padding: 0 20px; margin-top: 8px; margin-bottom: 14px;
.section-label { font-size: 12px; font-weight: 700; color: var(--text3);
                 letter-spacing: 0.5px; text-transform: uppercase; }
.section-more  { font-size: 12px; font-weight: 600; color: var(--accent); }
```

### iPad (`section-hd`)
```css
padding: 20px 20px 10px;
h2 { font: 700 12px/1; color: var(--text2); letter-spacing: .06em; text-transform: uppercase; }
.badge { background: var(--accent-dim); color: var(--accent2); font: 600 11px/1; padding: 3px 8px; border-radius: 100px; }
```

---

## Badges & Status Tags

```css
/* Status pill (inline) */
.proj-status { font: 500 11px/1; padding: 3px 8px; border-radius: 100px; }
.status-active { background: var(--green-dim); color: var(--green); }
.status-draft  { background: rgba(251,191,36,0.08); color: #FCD34D; }

/* Badge overlay (absolute, top-right of card) */
.bento-badge { font-size: 9px; font-weight: 700; padding: 3px 8px; border-radius: 100px; }
.badge-safe  { background: var(--green-dim);  color: var(--green);  border: 1px solid rgba(34,197,94,0.18); }
.badge-alert { background: var(--coral-dim);  color: var(--coral);  border: 1px solid rgba(244,63,94,0.18); }
.badge-ai    { background: var(--violet-dim); color: var(--violet); border: 1px solid rgba(139,92,246,0.18); }

/* Event tags */
.ev-tag { font-size: 9.5px; font-weight: 700; padding: 3px 8px; border-radius: 6px; }
.ev-tag.red    { background: var(--coral-dim);  color: var(--coral); }
.ev-tag.violet { background: var(--violet-dim); color: var(--violet); }
.ev-tag.sky    { background: var(--sky-dim);    color: var(--sky); }
.ev-tag.green  { background: var(--green-dim);  color: var(--green); }
```

---

## Alert Banner

```css
background: linear-gradient(135deg, rgba(244,63,94,0.18), rgba(249,115,22,0.12));
border: 1px solid rgba(244,63,94,0.28);
border-left: 3px solid var(--coral);   /* accent left stripe */
border-radius: var(--radius);
padding: 14px 16px;
```
- Pulse dot: `--coral`, 8px, glow `box-shadow` 2s pulse
- Shimmer sweep: `::after` left→right, 4s loop
- Slide-in animation on first appear

---

## Chat UI

### Phone Chat Input Bar
```css
/* Animated conic-gradient border (4s spin) */
conic-gradient: violet 0.6 → orange 0.6 → teal 0.5 → violet 0.6
background: rgba(40,40,46,0.75); backdrop-filter: blur(24px) saturate(180%);
border-radius: 100px;
```
Send button: `background: linear-gradient(135deg, var(--violet), var(--accent))`, circular 36px.

### Message Bubbles

| Type | Background | Border radius |
|---|---|---|
| Me (user) | `linear-gradient(violet 15%, orange 10%)` | `--radius --radius 6px --radius` (bottom-right flat) |
| AI / them | `var(--surface)`, `border: 1px solid var(--border2)` | `--radius --radius --radius 6px` (bottom-left flat) |
| Chat panel user (iPad) | `var(--accent-dim)`, `rgba(accent,0.15)` border | right-aligned, max-width 92% |
| Chat panel AI (iPad) | `var(--surface2)`, `var(--border2)` border | — |

### AI Action Cards (inside messages)
```css
background: var(--violet-dim);
border: 1px solid rgba(139,92,246,0.18);
border-radius: var(--radius-sm);
.ai-action-title { color: var(--violet); font-size: 12px; font-weight: 700; uppercase; }
```

### Chat Panel AI Orb (small inline icon)
```css
background: rgba(0,188,212,0.15);
border: 1.5px solid rgba(0,188,212,0.35);
/* always teal/cyan, regardless of persona accent */
```

---

## Authorship Bar

Human vs AI contribution indicator:

```css
.authorship-track { height: 8px; background: var(--surface3); border-radius: 100px; }
/* Human fill */   background: var(--green);   /* #22C55E */
/* AI fill */      background: var(--ai);       /* #22D3EE cyan */

/* Condensed strip (editor bottom) */
.auth-strip-fill { background: linear-gradient(90deg, var(--green) 68%, var(--ai) 68%); }
```

---

## Collab / AI Suggestion Banner (Yuki view)

```css
background: linear-gradient(135deg, rgba(192,132,252,0.15), rgba(0,188,212,0.1));
border: 1px solid rgba(192,132,252,0.2);
border-radius: var(--radius);
/* AI orb inside: teal rgba(0,188,212) */
/* Action pill: background:var(--ai-dim); border:rgba(0,188,212,0.3); color:var(--ai) */
```

---

## Stagger & Fade Animations

```css
.fade-in   { animation: fadeIn 0.5s var(--ease-out) both; }
@keyframes fadeIn { from { opacity:0; transform:translateY(10px) } to { opacity:1; transform:translateY(0) } }

/* Stagger classes */
.stagger-1 { animation-delay: 0.05s; }
.stagger-2 { animation-delay: 0.10s; }
.stagger-3 { animation-delay: 0.15s; }
.stagger-4 { animation-delay: 0.20s; }
.stagger-5 { animation-delay: 0.25s; }
```

Event list items use per-item delays: `nth-child(n)` with 0.07s increments.

---

## Accessibility

```css
/* Focus ring (WCAG 2.4.7) */
:focus-visible {
  outline: 2px solid var(--accent);
  outline-offset: 2px;
  border-radius: var(--radius-xs);
}
button:focus-visible { box-shadow: 0 0 0 3px var(--accent-dim); }
.nav-item:focus-visible { outline-offset: -2px; border-radius: 100px; }

/* Reduced motion (WCAG 2.3.1) */
@media (prefers-reduced-motion: reduce) {
  *, *::before, *::after {
    animation-duration: 0.01ms !important;
    transition-duration: 0.15s !important;
  }
  .page { transition: opacity 0.15s ease !important; transform: none !important; }
}
```

---

## App Logo / TrendLife Wordmark (Yuki view)

```css
.bloom-logo-icon {
  width: 28px; height: 28px; border-radius: 8px;
  background: linear-gradient(135deg, #9333EA, #C084FC);
  /* contains inline SVG icon */
}
.bloom-logo-text { font: 700 18px/1; letter-spacing: -0.5px; }
```

---

## Icons

> 完整 icon 規範（字型載入、常用 icon 對照表）請見根目錄 `design-conventions.md`。

**一律使用 Material Symbols Outlined，不使用 emoji。** 尺寸跟隨情境（nav 20px、bento 28px、action 18px），顏色跟隨 `currentColor`。

### 例外
- Kaleidoscope AI icon → 永遠用 `kaleidoscope-mandala.svg`（見 `constellation/design-conventions.md`）
- Status bar icons（signal / wifi / battery）→ 保持原始 inline SVG（見下節）

---

## Status Bar Icons

Both files use the same three inline SVG icons (signal, wifi, battery) with `fill="currentColor"`. Do not use emoji or system font characters for these.

---

## Gradients Quick Reference

| Use | Gradient |
|---|---|
| Home title keyword | `linear-gradient(135deg, var(--accent), var(--coral))` |
| AI action button | `linear-gradient(135deg, var(--violet), var(--accent))` |
| Profile avatar fallback | `linear-gradient(135deg, var(--violet), var(--accent))` |
| Chat send button (phone) | `linear-gradient(135deg, var(--violet), var(--accent))` |
| Showcase cover | `linear-gradient(135deg, pink 22%, lavender 18%, skyblue 14%)` |
| Canvas bottom fade | `linear-gradient(180deg, transparent 40%, var(--bg) 100%)` |
| Project thumbnails | e.g. `grad-music: linear-gradient(135deg, #312e81, #7c3aed, #c026d3)` |

---

## Project Thumbnail Gradients

```css
.grad-music { background: linear-gradient(135deg, #312e81, #7c3aed, #c026d3); }
.grad-art   { background: linear-gradient(135deg, #0c4a6e, #0284c7, #06b6d4); }
.grad-story { background: linear-gradient(135deg, #7c2d12, #dc2626, #ea580c); }
.grad-3d    { background: linear-gradient(135deg, #1e1b4b, #4338ca, #7c3aed); }
.grad-video { background: linear-gradient(135deg, #14532d, #16a34a, #65a30d); }
```
