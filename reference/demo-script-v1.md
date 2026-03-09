# TrendLife Demo Script v1

> 完整場景規劃，供 UX mockup 製作參考

---

## 場景 1：奶奶的健康檢查 + 防詐守護 (02:00 - 05:00)

### 便利性 — 健康管理智能分析
| 項目 | 內容 |
|------|------|
| 主 key | Jason Yy Huang (RD-AS) team |
| Demo | Line: 奶奶上傳健檢報告進行分析，AI管家回應健檢報告分析、推薦餐廳、預約門診 (三個動作) |
| | Line: 發送奶奶與AI管家互動的 summary 到 Eva 的 LINE chat |

**待設計：** AI管家為什麼知道需要執行這個發送 summary 給 Eva 的動作，需要設計一個機制用來 trigger 這個行為。

### 安全性 — 防詐守護即時攔截
| 項目 | 內容 |
|------|------|
| 主 key | Bert Huang (RD-AS) + Jason Yy Huang (RD-AS) team |
| Demo | TMSC app 攔截詐騙電話 (既有)，TMSC backend 通知 AI 管家後台詐騙電話阻擋事件 |
| | AI 管家發送攔截通知到 Eva 的 LINE chat |

**注意：** Bert 會跟 CA 那邊 sync，此方法只改 backend，不用動到 mobile app。

---

## 場景 2：Yvonne 的 IG 創作 + LINE 群組互動 (05:00 - 09:00)

### 便利性 — LINE 群組中的 AI 管家
| 項目 | 內容 |
|------|------|
| 主 key | Jason Yy Huang (RD-AS) team |
| Demo | Line: 給予 Yvonne 關於文案的引導性思考 (Wisdom Loop) |
| | Line group: 根據 Yvonne 的喜好 (memory) 推薦 IG 風格 |

**待確認：** Heather 提案新的 demo 內容 → 由 executor 做混音，需請 Jason 確認。

### 安全性 — 群組中的安全守護
| 項目 | 內容 |
|------|------|
| 主 key | Jason Yy Huang (RD-AS) team |
| Demo | Line group: 識別群組中的惡意連結、偵測網域安全風險，提供安全建議 |
| | Line group: chat bot 接收使用者的指示 (我們要聊小秘密了，請你離開)，或是三天到了自動離開 |

---

## 場景 3：Eva 的晚餐混亂管理 (09:00 - 12:00)

### 便利性 — Chaos Management
| 項目 | 內容 |
|------|------|
| 主 key | Jason Yy Huang (RD-AS) team |
| Demo | Line: 主動提醒 → 先生到家時間、Yvonne 的約會、Ethan 運動完很餓、奶奶的低鹽低糖要求，給出建議，訂 Uber 或是使用冰箱的食材料理、給推薦食譜 (REI 家庭憲法、可查看冰箱存量) |
| | Line: 使用 Uber Eat 點餐，為每個人的需求訂閱適合的餐點，抵達確認畫面 (無需實際下訂) |

**待確認：** REI 家庭憲法概念剛引入，我們有能力查看冰箱存量嗎？如何進行？

### 安全性 — 資料保護與脫敏
| 項目 | 內容 |
|------|------|
| 主 key | UX team + Jason Yy Huang (RD-AS) team 協助 |
| Demo | 使用 mockup 示意脫敏是如何完成的，這部分通常在後台完成，不會有使用者看到的內容 |

---

## 場景 4：Eva 回家前的智能準備 + IoT 安全 (12:00 - 15:00)

### 便利性 — 智能家居自動準備
| 項目 | 內容 |
|------|------|
| 主 key | Jason Yy Huang (RD-AS) |
| Demo | Eva 預定回家時間為 6:30，請 AI 管家在這時調整智慧家居的設定 |
| | AI管家使用 Line 發訊給 Eva，告知將會調整家中環境 (executor 任務調整 IoT) |

**注意：** 目前可用 mobile app 控制掃地機器人，現場 demo 也會試智慧電燈之類的，實際上能操作的 IoT 視能準備的設備為主。

### 安全性 — IoT 設備異常攔截
| 項目 | 內容 |
|------|------|
| 主 key | Bert Huang (RD-AS) + Jason Yy Huang (RD-AS) team |
| Demo | CloudEdge: 發送安全威脅通知給 AI 管家 (連接未知 IP, 上網流量異常) |
| | Line: 通知安全威脅的處理結果 |

---

## 場景 5：全家視角整合（Graph RAG）(15:00 - 17:00)

### 隱私控制 & Graph
| 項目 | 內容 |
|------|------|
| 主 key | UX team |
| Demo | Demo 隱私設定的介面 |

**注意：** 不需要有實際的功能，以 UI 示意為主。

---

## 場景 6：彈性與擴展（備考模式）(17:00 - 18:00) — ~~已刪除~~

> **此區段刪除。** 下班前討論確認不需要 live demo，略過此場景。

原內容備考：
- Line: 女兒在 AI 管家的對話中提示進入備考模式，在後續的對話中，做考試以外的事要提醒她

---

## 結尾：週日晚餐溫馨收尾 (18:00 - 20:00)

| 項目 | 內容 |
|------|------|
| 主 key | UX team |
| Demo | 當天的 summary |

**注意：** 不需要有實際的功能，以 UI 示意為主。

---

## 負責人總覽

| 負責人 | 負責場景 |
|--------|----------|
| Jason Yy Huang (RD-AS) | 場景 1-4 主要功能 |
| Bert Huang (RD-AS) | 場景 1 防詐攔截、場景 4 IoT 安全 |
| UX team | 場景 3 脫敏、場景 5 Graph RAG、結尾 |

## 待確認事項

1. AI管家 trigger 機制：如何判斷要主動發 summary 給 Eva？
2. Heather 的混音 executor 提案：需 Jason 確認
3. REI 家庭憲法 + 冰箱存量查看能力
4. 現場 IoT 設備清單（掃地機器人 / 智慧電燈等）
