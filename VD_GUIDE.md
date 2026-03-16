# VD 使用說明：用 Claude Code 協作 UI Mockup

> 你不需要懂 git。所有版本控制操作都由 Claude 代勞。

---

## 第一次使用（只做一次）

請 Karen 幫你完成以下設定：

1. 安裝 Claude Code（已完成 ✓）
2. Clone repo 到本機
3. 建立你的工作 branch

設定完成後，Karen 會告訴你：
- **你的 branch 名稱**（例如：`vd/yuki-view`）
- **你負責的檔案路徑**（例如：`constellation/mockup-yuki-ipad.html`）

把這兩個資訊記下來，之後會用到。

---

## 每次開工

**1. 開啟 terminal，進入專案資料夾**

```
cd trendlife-ui-mockup
```

**2. 告訴 Claude 你今天要做什麼**

```
claude
```

啟動後，第一句話說：

> 「我今天要改 `constellation/mockup-yuki-ipad.html`，branch 是 `vd/yuki-view`，請先 pull 最新版本」

Claude 會自動切換 branch、拉最新版本，然後問你想改什麼。

---

## 怎麼描述修改

直接用中文說就好，不需要寫程式碼。

**範例：**

| 你說的話 | Claude 會做的事 |
|--------|--------------|
| 「S3 的卡片背景改成深藍色 `#1a2744`」 | 找到 Screen 3 的卡片，修改背景色 |
| 「標題字體縮小，大概 18px」 | 調整對應 CSS |
| 「在右上角加一個設定 icon」 | 加入 icon 元素 |
| 「S5 跟 S3 的間距看起來不一致，對齊一下」 | 比對兩個 screen 的 padding |

**不確定時，先問：**
> 「你覺得這樣的改動合理嗎？先跟我說想法，不要直接改」

---

## 確認修改結果

每次修改後，你可以說：

> 「在瀏覽器開給我看」

Claude 會告訴你怎麼在本機預覽（直接用瀏覽器開 HTML 檔案）。

確認沒問題後說：

> 「好，可以 commit」

Claude 會自動 commit 並 push 到你的 branch。

---

## 不確定改得對不對？

說：「先不要 commit，我想再看一下」

Claude 會等你確認。

---

## 改完之後

你不需要做任何事。Karen 會收到通知，review 後 merge 到主版本。

如果 Karen 在 GitHub 上留了修改意見，她會直接傳訊息告訴你，你再開 Claude 繼續改就好。

---

## 常見問題

**Q：我不小心說錯了，Claude 改錯怎麼辦？**
> 說「還原剛才的修改」，Claude 會 undo。

**Q：我想看目前改了哪些地方？**
> 說「顯示今天改了什麼」

**Q：Claude 問了我看不懂的問題？**
> 截圖傳給 Karen。

---

*如有任何問題，聯絡 Karen。*
