# Mayumi 視角 Demo 腳本

> 對應 PDF Act 2（危機協調）＋ Act 3（深夜報告）
> 錄製目標：mockup-mei-v2.html，手機尺寸，含點擊動畫

---

## 場景摘要

### S1 — 開場

**中文：** Mei 的手機首頁靜止顯示，頂部 BP Alert banner 醒目閃爍，說明奶奶的血壓警報已在系統上出現。

**EN：** Mei's home screen sits idle with a pulsing BP Alert banner at the top, showing that Grandma's blood pressure alert has already surfaced in the system.

---

### S2 — 危機通報

**中文：** Mei 點擊警報 banner，進入奶奶的健康報告。頁面顯示 168/112 mmHg（Stage 2 高血壓），Kaleidoscope 已即時偵測並通知。

**EN：** Mei taps the alert banner and lands on Grandma's health report showing 168/112 mmHg — Stage 2 Hypertension. Kaleidoscope detected and surfaced this in real time.

---

### S3 — AI 跨成員協調

**中文：** Mei 切換至 Kaleidoscope AI Chat，系統已自動發起跨家庭成員的危機協調，對話紀錄捲動至底，呈現完整 AI 介入過程。

**EN：** Mei switches to Kaleidoscope AI Chat, where the system has already begun coordinating across family members. The conversation scrolls to reveal the full AI-driven crisis response.

---

### S4 — 晚間報告：Yuki 的成長

**中文：** Mei 回到首頁，在星座圖中點擊 Yuki 的頭像，進入成員詳情，再點選「View growth report」查看 Yuki 今日的創作報告——原創比例與 AI 使用情況一目了然。

**EN：** Mei returns to home and taps Yuki's avatar on the constellation map, opening her member detail. She then taps "View growth report" to review Yuki's creative work for the day — originality score and AI usage at a glance.

---

### S5 — 防護報告：Safety

**中文：** Yuki 的報告捲動完畢後，Mei 回到首頁，點擊 Protection bento card 進入安全報告，瀏覽今日攔截的詐騙電話與危險連結紀錄。

**EN：** After reviewing Yuki's growth report, Mei returns home and taps the Protection bento card to open the Safety report, scrolling through today's blocked scam calls and dangerous links.

---

## 操作細節

| 幕 | 進入方式 | View | 捲動 |
|---|---|---|---|
| S1 | 起始畫面 | `v-home` | 無 |
| S2 | 點 BP Alert banner | `v-health` | 停留 2s → 捲動 |
| S3 | 點底部 Kaleidoscope nav | `v-ai` | 停留 2s → 捲動至底 → 停留 2s |
| S4 | 點底部 Home → Yuki 頭像 → View growth report | `v-detail` → `v-yuki` | 無 |
| S5 | 承接 S4；停留 2s → 捲動；回 Home → 點 Protection | `v-yuki` → `v-home` → `v-safety` | 兩段捲動 |

## 技術實作
- 點擊動畫：白色半透明 ripple，注入 `mockup-mei-v2.html`
- 自動化：Playwright 腳本（`record-mayumi.js`）
- 輸出格式：`.webm`，輸出路徑：`../outputs/`
- `tapAndNav`：ripple 先顯示 450ms，再 evaluate 跳頁
- 每個畫面進入後先停留 2 秒再捲動
