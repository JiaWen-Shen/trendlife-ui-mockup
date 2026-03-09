# TrendLife Mockup Plan v1

> 供新 session 無縫繼續使用的完整工作計畫
> 最後更新：2026-03-05

---

## 專案基本資訊

- **專案路徑**：`/Users/karen_shen/Jottacloud/trendlife-ui-mockup/`
- **主要 mockup 檔案**：`mockup-scene1-standalone.html`（同時存在 `mockup-scene1.html`，兩者內容相同，`index.html` 會 redirect 到 standalone 版）
- **品牌色彩**：已定義在 CSS `:root`，以 `--red: #D71920` 為主色，`--navy: #1C2B35`、`--teal: #0093A7`、`--cream: #F5EFE8`
- **字型**：Geist（Google Fonts），fallback `-apple-system`
- **裝置尺寸**：390px 寬，844px 高（iPhone 14 Pro），桌面版置中顯示
- **Logo**：`reference/logo-mark-only.png`（用於 AI Butler avatar）

## 參考資料位置

| 檔案 | 說明 |
|------|------|
| `ref/TrendLife_AI_Demo_Story_Line_v12_embedded.html` | 完整 Demo 劇本 v12，含所有場景分鏡、對話內容、解說文字（最重要參考） |
| `ref/Kaleidoscope v3.pdf` | 技術架構文件（AI Agent 架構、Memory 系統、Executor POC）|
| `ref/Kaleidoscope_Chandler_UI_Brief_v5_完整版.html` | Kaleidoscope UI 簡報 v5（場景敘事、設計理念框）|
| `ref/TrendLife_StyleBoard_Round4.pdf` | 品牌風格板 |
| `ref/from peter Mar3/kaleidoscope-demo 1.html` | React + Tone.js 的互動展示（Kaleidoscope v7）|
| `reference/demo-script-v1.md` | 從會議討論整理的 Demo Script（場景負責人、待確認事項）|
| `reference/logo-full-transparent.png` | 全版 logo |
| `reference/logo-mark-only.png` | Logo mark（用於 avatar）|

## 技術架構重點（供 mockup 視覺設計參考）

來自 Kaleidoscope v3.pdf：

```
Client App (LINE / Mobile)
    ↓
Main AI Agent  ←→  Trend Secure Control (PII Masking)
    ↓
L1 Agents (per-person, 1st-line interface)
    ↓
L2 Agent (family-wise, coordinates executor, scheduled tasks)
    ↓
Executor ←→ Memory
    ↓
Browser(Playwright) / Android(ADB) / API / Matter Protocol(IoT)
```

### Memory 四類型

| 類型 | 範圍 | 用途 |
|------|------|------|
| Current Context | Individual / Private | 短期當前對話 |
| Retrieval Memory | Individual / Shared | 長期 Summary/Subject/Profile |
| Family Core | Family / Shared | 家庭價值觀、REI 憲法 |
| Task Memory | Agent / Shared | Skills / Knowledge（Executor 用）|

### Memory 雙層架構（Scene 5 Graph RAG 視覺化依據）

- **Vector Store**：User-ID + Vector + Summary，語義相似搜尋（Top-k）
- **Graph Memory**：Triple（Subject, Relation, Object），Graph traversal，支援 parental visibility

### Executor 已驗證 POC

- Browser: UberEat 點餐、長庚掛號（Playwright）
- Android: 掃地機器人（ADB + Accessibility API）
- Protocol: Matter（IoT 設備）

---

## 現有 Screens 狀態（Screens 0–13）

| Screen ID | 名稱 | 場景 | 完整度 |
|-----------|------|------|--------|
| screen-0 | Eva Home（家人狀態列、待辦日曆、通知中心）| 通用 | ✅ 完整 |
| screen-1 | 奶奶 LINE chat（上傳健檢報告 → AI 分析）| 場景 1 | ⚠️ 需補三個動作 |
| screen-2 | Eva 健康報告詳情（脫敏摘要）| 場景 1 | ⚠️ 需加推薦餐廳 |
| screen-3 | 確認預約門診 | 場景 1 | ✅ 完整 |
| screen-4 | 預約完成 | 場景 1 | ✅ 完整 |
| screen-5 | Fraud Blocked — Eva 收到攔截通知 | 場景 1 | ✅ 完整 |
| screen-6 | 奶奶手機：詐騙電話攔截（TMSC 全螢幕警示）| 場景 1 | ✅ 完整 |
| screen-7 | 掛斷後畫面 | 場景 1 | ✅ 完整 |
| screen-8 | 新增提醒表單（家人選擇、提醒方式）| 通用 | ✅ 完整 |
| screen-9 | Todo Detail | 通用 | ✅ 完整 |
| screen-10 | Dinner AI Execution（AI 處理晚餐）| 場景 3 | ⚠️ 需加每人個別餐點 |
| screen-11 | 餐廳推薦列表 | 場景 3 | ✅ 完整 |
| screen-12 | 訂單確認（Din Tai Fung，5 members）| 場景 3 | ✅ 完整 |
| screen-13 | 已完成任務記錄 | 通用 | ✅ 完整 |

---

## 完整工作清單

> 格式：`[優先級] [Screen ID] 畫面名稱 — 說明`

---

### OPENING：混亂的週五下午（全新）

**N-01** 🔴 `screen-opening-1`：**Eva 的通知轟炸畫面**
- 手機鎖定螢幕或通知中心，同時出現 6 則通知：
  1. LINE：奶奶傳來健康檢查報告照片
  2. LINE：Yvonne 的群組（20 則未讀）
  3. LINE：學校通知「家長會改期」
  4. Email：醫院預約確認信
  5. WhatsApp：先生「今晚會晚回」
  6. 簡訊：「您有包裹未領取...」（詐騙風格）
- Eva 旁白：「每天下午都是這樣... 我根本分不清輕重緩急」
- 視覺：訊息泡泡堆疊動畫，畫面感覺混亂

**N-02** 🔴 `screen-opening-2`：**AI 管家登場過渡**
- TrendLife logo 出現，管家頭像浮現
- 卡片文字：「讓我來幫您整理這一切」
- Peter 解說框（可選）：「如果您有一位 24/7 的 AI 管家...」
- 導向 → screen-0（Eva Home）

---

### 場景 1：修改項目

**修 S-01** 🟡 `screen-1`（已存在）：**奶奶 LINE chat — 補完三個動作**
- 現狀：只顯示「分析完成」
- 補充：分析完成後顯示三個 action cards：
  1. 📊 健康分析完成（血糖略高）
  2. 🍽️ 推薦 3 間低 GI 餐廳（已篩選）
  3. 📅 已幫奶奶預約心臟科門診（待 Eva 確認）
- 加上「Summary 已同步給 Eva」的確認訊息

**修 S-02** 🟡 `screen-2`（已存在）：**Eva 健康報告詳情 — 補推薦餐廳**
- 現狀：只有健康指標摘要
- 補充：在下方加入「推薦餐廳」區塊（3 間低 GI 餐廳卡片）
- 加入「[確認預約]」按鈕（→ screen-3）

**N-03** 🔴 `screen-vault-1`：**Security Vault 脫敏流程視覺化**
- 視覺化資料流（漫畫式）：
  ```
  奶奶的健檢報告（原始）
      ↓
  Trend Secure Control（PII Masking）
      ↓ 脫敏後              ↓ 本地保存
  送給 Cloud LLM        Security Vault
  ✓ 血糖數值略高         完整原始資料
  ✓ 血壓偏高             林○美花
  ✗ 姓名 / 身分證        身分證：A1234...
  ✗ 完整病歷             完整血檢數值
  ```
- 標注：「智能資料脫敏引擎 — 敏感資料不給 AI 公司，TrendLife 企業級加密本地儲存」
- Frank 解說框：「符合 GDPR、個資法、醫療法」

**N-04** 🟡 `screen-eva-summary`：**Eva 收到奶奶互動 summary 推播**
- Eva 的 TrendLife APP 收到推播
- 內容：「Eva，奶奶的健康檢查報告已分析完成」
- Trigger 機制說明卡（Frank 說明）：
  - L1 Agent（奶奶）→ 偵測到需要家庭協調 → 通知 L2 Agent → L2 Agent 推播給 Eva（基於 Family Core Memory 設定「奶奶健康事件需通知 Eva」）
- 選項：[查看完整報告] [確認預約] [發送關心給奶奶]

---

### 場景 2：Yvonne 的 IG 創作 + LINE 群組（全新）

**N-05** 🔴 `screen-yvonne-1`：**Yvonne LINE 個人對話 — Wisdom Loop**
- 時間：週五晚上 8:00 PM
- Yvonne 問：「管家，我想幫我們的創作小組寫一個 IG 文案，主題是『青春』」
- AI 回應顯示三個版本卡片（可左右滑動）：
  - 版本 A（活潑）：「那個夏天，我們笑得最大聲 ☀️」
  - 版本 B（知性）：「青春不是年紀，是敢於不確定的勇氣」
  - 版本 C（簡約）：「here. now. us.」
- AI 追問（Wisdom Loop）：「你覺得哪個最能代表你？為什麼？」
- 設計理念框：「AI 展示不確定性，引導思考 — 不是給答案，是培養判斷力」

**N-06** 🔴 `screen-yvonne-2`：**LINE 群組 — AI 管家加入 + IG 風格推薦**
- 群組名稱：「Yvonne + Alice + Mia 的創作小組」
- 對話流程：
  - Alice：「我們週末的 IG 圖要用什麼風格？」
  - Mia：「復古膠片風？還是極簡黑白？」
  - Yvonne：「讓我問問我的 AI 管家～」→ 把 TrendLife AI 管家加入群組
  - Yvonne @管家：「我們想做一張 IG 圖，主題是『青春』，有什麼建議？」
  - AI 管家回應：「根據 Yvonne 的風格喜好（Memory）推薦：柔和日系風格（配色 #FFF5E1 + #FFB6C1，字體思源黑體 Light），免費素材推薦 Unsplash 已篩選 5 張。要我整理到設計板嗎？」
  - Alice & Mia：「哇，這個管家好厲害！」

**N-07** 🔴 `screen-yvonne-3`：**惡意連結即時攔截**
- 接續 N-06 群組，Mia 貼出連結：`design-pro-free[.]tk/download`
- AI 管家即時警告卡（紅色警示）：
  - ⚠️ 安全提醒
  - 網域註冊僅 5 天（高風險）
  - 已被標記為釣魚網站
  - 可能竊取帳號密碼
  - 建議替代：Canva（免費版）/ Figma（學生方案）
- Alice：「哇，好險！差點就點了」
- Mia：「Yvonne 你這個管家也太厲害了吧！」
- Alice：「我也想要！怎麼申請？」
- Yvonne：「哈哈我媽幫全家裝的，叫 TrendLife AI 管家」
- 標注框：「Teenager 之間的口碑傳播 — 同儕推薦比家長要求更有效」

**N-08** 🟡 `screen-yvonne-4`：**AI 管家自動退出通知**
- 時間標記：3 天後
- LINE 群組系統通知：「TrendLife AI 管家 已離開群組」
- AI 管家訊息：「群組已 72 小時沒有 @ 我了，為了尊重大家的隱私，我先退出囉～有需要隨時可以再把我加回來 👋」
- Alice：「哇，這個管家還會自己離開？」
- Yvonne：「對啊，不會一直待在群組裡」
- Mia：「好貼心！完全不會有被監視的感覺」
- 機制說明卡：「群組閒置 72 小時（可調整）→ 主動離開 → 不留痕跡 → 隨時可再邀請」

**N-09** 🟡 `screen-yvonne-5`：**Yvonne 的 Memory Graph RAG 視覺化**
- 節點圖，中心：「Yvonne 的設計風格偏好」
- 學習來源節點（都來自主動互動）：
  - 「幫我找日系風格配色」→ 記住：日系、溫暖色調
  - 「用思源黑體做設計」→ 記住：思源黑體
  - 與 Alice、Mia 的協作 → 記住：協作夥伴
  - 「我喜歡柔和配色」→ 記住：柔和風格
- 標注：「AI 只記住 Yvonne 主動分享的內容，不追蹤瀏覽歷史、不監控行為」
- Vector Store 標注（語義搜尋）vs Graph Memory 標注（關係推理）

---

### 場景 3：晚餐混亂管理（修補）

**N-10** 🔴 `screen-dinner-1`：**Eva 主動提醒通知（晚餐起點）**
- Eva 還在開會，AI 管家主動推播：
  - 今晚晚餐提醒：
  - 先生 7:00 PM 到家
  - Yvonne 要趕 8:30 PM 線上討論
  - Ethan 足球練習剛結束（很餓）
  - 奶奶需要低鹽低糖
  - 建議方案 A：訂 Uber Eats（30 分鐘內送達）
  - 建議方案 B：使用冰箱現有食材（番茄炒蛋 + 青菜，15 分鐘）
- Eva 點選「訂 Uber Eats」→ 進入 screen-10

**N-11** 🟡 `screen-rei-1`：**REI 家庭憲法 / Executor 授權設定**
- 標題：「家庭 AI 授權設定」
- 列表（每個 action 的授權狀態）：
  - 查看冰箱存量（已授權 ✓）
  - 建議食譜（已授權 ✓）
  - 查看行事曆（已授權 ✓）
  - 推薦餐廳（已授權 ✓）
  - 直接下訂餐點（⚠️ 需確認）
  - 控制 IoT 設備（⚠️ 需確認）
  - 發訊息給家人（⚠️ 需確認）
- 說明框：「REI 家庭憲法：每個家庭決定 AI 的權限邊界，不是平台決定，是你決定」

**修 S-10** 🟡 `screen-10`（已存在）：**Dinner 加每人個別餐點分配**
- 補充每人餐點卡片：
  - 奶奶：低鹽低糖便當
  - Yvonne：素食義大利麵
  - Ethan：兒童牛排餐
  - 先生 + Eva：綜合套餐
  - 預計 6:15 PM 送達

**N-12** 🟡 `screen-vault-2`：**資料脫敏流程（場景 3 晚餐版）**
- 送給 AI 的：✓「需要 4 人份晚餐」/ ✓「一位成員需要低鹽低糖」/ ✓「一位成員吃素」
- 不送給 AI：✗ 奶奶的血糖報告 / ✗ 飲食限制的醫療診斷 / ✗ 家庭成員姓名年齡
- 完整資料存在 Security Vault：Trend Micro 企業級加密，不送給 OpenAI/Google

---

### 場景 4：Eva 回家前 + IoT 安全（全新）

**N-13** 🔴 `screen-iot-1`：**Eva 收到回家準備推播**
- 手機推播：「您預計 6:30 PM 到家，我已開始準備家裡環境」
- 點開後看到 IoT 操作清單（→ N-14）

**N-14** 🔴 `screen-iot-2`：**L2 Agent → Executor 任務治理畫面**
- 標題：「AI 管家正在執行家居準備」
- 任務清單（L2 Agent 分配給 Executor）：
  - ✅ 智能門鎖：預熱感應（靠近自動解鎖）— 已授權
  - ✅ 智能燈光：客廳 + 廚房 溫暖色溫 2700K — 已授權
  - ✅ 空調：調整至 24°C — 已授權
  - ✅ 掃地機器人：回到充電座（Matter protocol）— 已授權
  - ✅ 智能窗簾：關閉（隱私模式）— 已授權
  - ⚠️ 訂購缺少食材（羅勒葉，預估 $80）— 需確認
- 說明框：「Agentic AI 行動治理：從 GenAI（對話）到 Agentic AI（行動）的時代，最大風險是 AI 做錯事，行動治理確保每個動作都有適當授權」
- [核准] [拒絕] 按鈕（針對需確認項目）

**N-15** 🟡 `screen-iot-3`：**管家分身架構示意（3 步驟安裝）**
- 標題：「管家分身：讓 AI 住進您家」
- 步驟：
  1. 下載 TrendLife 家庭版安裝包
  2. 在家裡 PC 上安裝（5 分鐘）
  3. 掃描 QR Code 綁定帳號
- 架構圖：
  - 雲端 TrendLife AI 管家 ↔ 自動同步 ↔ 家裡 PC 上的管家分身
  - 本地控制 IoT（毫秒級回應）、24/7 監控家庭網路
  - 所有 IoT 控制記錄不上傳雲端

**N-16** 🔴 `screen-iot-4`：**IoT 安全警報畫面**
- ⚠️ 安全警報（紅色全螢幕或大卡片）
- 客廳智能攝影機異常：
  - 深夜 2:00 AM 突然啟動（非正常時間）
  - 嘗試連接未知 IP：45.xxx.xxx.xxx（東歐）
  - 上傳流量異常：平時 100KB → 現在 500MB
  - TrendLife 判定：疑似被駭客入侵
- 管家已執行：
  - 隔離該攝影機網路權限 ✓
  - 封鎖可疑 IP 連線 ✓
  - 停止異常資料傳輸 ✓

**N-17** 🔴 `screen-iot-5`：**IoT 威脅處理結果通知**
- 結果卡：「客廳智能攝影機疑似被駭，已自動隔離，家庭網路安全無虞」
- 選項：[查看詳情] [重置設備] [聯絡客服]
- Frank 解說框：「智能家居的隱藏風險：一個被駭裝置可影響全家網路。TrendLife 管家分身 24/7 監控所有智能裝置，發現異常立即切斷。」
- 監控項目標注：設備連線時間 / 流量大小 / 連線目的地 / 韌體版本

---

### 場景 5：全家視角整合 Graph RAG（全新）

**N-18** 🔴 `screen-graph-1`：**Eva 詢問今日家庭狀況**
- Eva：「今天家裡狀況如何？」
- AI 管家回覆 overview → 點擊進入 N-19

**N-19** 🔴 `screen-graph-2`：**家庭隱私控制設定頁**
- 標題：「TrendLife 家庭共享設定」
- 每個家庭成員的分享開關：
  - 奶奶（已同意分享）：健康提醒 ✓ / 位置資訊 ✗ / 通話內容 ✗
  - Yvonne（已同意分享）：學習進度 ✓ / LINE 群組安全 ✓ / 個人訊息內容 ✗
  - Ethan（已同意分享）：運動記錄 ✓ / 遊戲時間 ✓ / 瀏覽記錄 ✗
  - 先生：工作行事曆（到家時間）✓ / 其他 ✗
- 說明：「每個人都能隨時調整分享設定」

**N-20** 🔴 `screen-graph-3`：**家庭 Graph RAG 雙層全覽視圖**
- 中心節點：Eva 的家庭
- 成員節點（顏色標示）：
  - 奶奶 🟢：健康已處理 / 安全：攔截 1 次詐騙
  - Yvonne 🟡：學習進行中 / 安全：攔截 1 次惡意連結 / 社交：與 Alice 協作
  - Ethan 🟢：足球練習完成 / 遊戲：今日額度剩 30 分鐘
  - 先生 🟢：7:00 PM 返家
- 底部雙層標注：
  - Vector Store：快速語義搜尋（「奶奶飲食限制」→ Top-k 相關記憶）
  - Graph Memory：Triple 關係推理（奶奶 → needs → 低鹽飲食）
- AI 能看到 vs 看不到的明確區分

**N-21** 🟡 `screen-graph-4`：**每個成員的個別視角（4 手機並排）**
- Eva：全家 overview（基於大家同意分享的資訊）
- Yvonne：自己的 full detail + 隱私控制開關
- Ethan：遊戲時間 + 功課 + 可調整設定
- 奶奶：健康提醒 + 隨時可關閉分享

---

### 結尾：週日晚餐溫馨收尾（全新）

**N-22** 🟡 `screen-ending-1`：**本週家庭 Summary 卡片**
- 卡片設計（精美大卡，深色背景）：
  - 本週家庭狀況
  - ✓ 9 次安全防護
  - ✓ 15 個主動建議
  - ✓ 0 次隱私外洩
- Eva 旁白：「以前週末我都在追進度，現在我可以真正陪伴家人，因為我知道 AI 管家會幫我守護一切」

**N-23** 🟡 `screen-ending-2`：**下週重點預覽**
- 下週重點：
  - Yvonne 升學面試（週三）
  - Ethan 足球比賽（週六）
  - 奶奶回診（週五）
- Peter 三大承諾卡：
  1. 主動分享，不是被動監控
  2. 個人控制，不是家長控制
  3. 家庭協作，不是監控系統
- 結語：「TrendLife AI 管家：不只是 AI，是您家的守護者」

---

## 畫面導航規劃

```
Opening: N-01 → N-02 → screen-0 (Eva Home)

場景 1（從 screen-0 點奶奶）:
  screen-0 → screen-1 → [N-03: Vault 視覺化] → screen-2 → screen-3 → screen-4
  screen-0 → [N-04: Summary 推播]
  screen-0 → screen-5 → screen-6 → screen-7

場景 2（從 screen-0 點 Yvonne）:
  screen-0 → N-05 → N-06 → N-07 → N-08 → N-09

場景 3（從 screen-0 點晚餐）:
  screen-0 → N-10 → N-11（REI 設定）
  N-10 → screen-10 → screen-11 → screen-12 → N-12（Vault）

場景 4（從 screen-0 點 Eva 回家）:
  screen-0 → N-13 → N-14 → N-15（分身架構）
  N-14 → N-16 → N-17

場景 5（從 screen-0 點 Graph RAG）:
  screen-0 → N-18 → N-19 → N-20 → N-21

結尾:
  screen-0 → N-22 → N-23
```

---

## 數字總覽

| 項目 | 數量 |
|------|------|
| 現有可沿用 Screens | 11 |
| 需修改的 Screens | 3（S1, S2, S10）|
| 全新 Screens | 23 |
| **預計總 Screens** | **~37** |

---

## 建議實作順序

1. **Opening** (N-01, N-02) — 建立第一印象
2. **場景 2 LINE 群組** (N-05 ~ N-08) — 最多全新畫面，且 demo 中是視覺亮點
3. **場景 4 IoT** (N-13 ~ N-17) — 技術深度展示
4. **場景 5 Graph RAG** (N-18 ~ N-21) — 最後技術高潮
5. **場景 1 修補** (修S1, 修S2, N-03, N-04) — 補強現有
6. **場景 3 修補** (N-10 ~ N-12, 修S10) — 補強現有
7. **結尾** (N-22, N-23)

---

## 未解決事項（待業務確認，不影響 mockup 製作）

1. AI 管家 trigger 機制（如何知道要發 summary 給 Eva）— 架構層已解（L2 Agent 基於 Family Core Memory），mockup 用說明卡呈現即可
2. Heather 的混音 Executor 提案（場景 2，Jason 確認中）
3. REI 家庭憲法 + 冰箱存量查看能力（場景 3）
4. 現場 IoT 設備清單（場景 4）
5. Kaleidoscope v3.pptx 是加密檔案 — 已用 PDF 版讀取，內容為技術架構（不影響 mockup）
