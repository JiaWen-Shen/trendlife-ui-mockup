/**
 * Mayumi Demo Recording Script
 * Playwright 自動操作 mockup-mei-v2.html，輸出含點擊動畫的 .webm 影片
 *
 * 使用方式:
 *   node demo-scripts/record-mayumi.js
 */

const { chromium } = require('playwright');
const path = require('path');
const fs = require('fs');

const FILE_URL = 'file://' + path.resolve(__dirname, '../constellation/mockup-mei-v2.html');
const OUTPUT_DIR = path.resolve(__dirname, '../outputs');

fs.mkdirSync(OUTPUT_DIR, { recursive: true });

// ── 點擊動畫 CSS ──────────────────────────────────────────────────────────────
const RIPPLE_CSS = `
  .click-ripple {
    position: fixed;
    width: 60px;
    height: 60px;
    border-radius: 50%;
    background: rgba(255, 255, 255, 0.45);
    border: 2px solid rgba(255, 255, 255, 0.8);
    transform: translate(-50%, -50%) scale(0);
    animation: clickRipple 0.65s cubic-bezier(0.16, 1, 0.3, 1) forwards;
    pointer-events: none;
    z-index: 999999;
  }
  @keyframes clickRipple {
    0%   { transform: translate(-50%,-50%) scale(0);   opacity: 1; }
    100% { transform: translate(-50%,-50%) scale(2.8); opacity: 0; }
  }
  /* 確保 view 轉場動畫在 headless 錄製時仍正常執行 */
  .view {
    transition: opacity 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important,
                transform 0.4s cubic-bezier(0.16, 1, 0.3, 1) !important;
  }
`;

async function injectClickRipple(page) {
  await page.addStyleTag({ content: RIPPLE_CSS });
  await page.evaluate(() => {
    document.addEventListener('click', (e) => {
      const d = document.createElement('div');
      d.className = 'click-ripple';
      d.style.left = e.clientX + 'px';
      d.style.top = e.clientY + 'px';
      document.body.appendChild(d);
      setTimeout(() => d.remove(), 750);
    }, true);
  });
}

// 在指定座標顯示 ripple
async function showRipple(page, x, y) {
  await page.evaluate(({ x, y }) => {
    const d = document.createElement('div');
    d.className = 'click-ripple';
    d.style.left = x + 'px';
    d.style.top = y + 'px';
    document.body.appendChild(d);
    setTimeout(() => d.remove(), 750);
  }, { x, y });
}

// 取得元素中心座標，顯示 ripple → 等 450ms → 用 evaluate 跳頁
// 確保點擊特效在畫面轉換前已清楚顯示
async function tapAndNav(page, selector, viewIdx) {
  const box = await page.locator(selector).boundingBox();
  if (box) {
    const cx = Math.round(box.x + box.width / 2);
    const cy = Math.round(box.y + box.height / 2);
    await showRipple(page, cx, cy);
  }
  await sleep(450);  // ripple 先撐開，再觸發跳頁
  await page.evaluate((idx) => switchView(idx), viewIdx);
}

function sleep(ms) {
  return new Promise(r => setTimeout(r, ms));
}

// 慢速向下捲動，containerSel 為完整 CSS selector
async function slowScroll(page, containerSel, distance = 280, durationMs = 2000) {
  const steps = 50;
  const stepDelay = durationMs / steps;
  const stepDist = distance / steps;
  for (let i = 0; i < steps; i++) {
    await page.evaluate(({ sel, dy }) => {
      const el = document.querySelector(sel);
      if (el) el.scrollTop += dy;
    }, { sel: containerSel, dy: stepDist });
    await sleep(stepDelay);
  }
}

// 重置捲動位置至頂部
async function resetScroll(page, containerSel) {
  await page.evaluate((sel) => {
    const el = document.querySelector(sel);
    if (el) el.scrollTop = 0;
  }, containerSel);
}

// ── Main ──────────────────────────────────────────────────────────────────────
(async () => {
  const browser = await chromium.launch({ headless: true });

  const context = await browser.newContext({
    viewport: { width: 375, height: 812 },
    recordVideo: {
      dir: OUTPUT_DIR,
      size: { width: 375, height: 812 },  // 與 viewport 一致，靠 deviceScaleFactor 提升清晰度
    },
    deviceScaleFactor: 3,  // 3x DPI 渲染，畫面更銳利
  });

  const page = await context.newPage();
  console.log('Opening:', FILE_URL);
  await page.goto(FILE_URL, { waitUntil: 'domcontentloaded' });
  await sleep(1500);
  await injectClickRipple(page);

  // ── S1: Home 畫面 — BP Alert banner 醒目顯示（3 秒）────────────────────────
  console.log('S1: Home');
  await sleep(2000);

  // ── S2: 點 Alert Banner → Health → 停留 3 秒 → 捲到底 → 跳轉 ──────────────
  console.log('S2: Tap Alert Banner → Health → 3s pause → scroll to bottom');
  await showRipple(page, 187, 206);
  await sleep(450);
  await page.evaluate(() => switchView(5));
  await sleep(600);
  await sleep(2000);  // 停留 2 秒後開始捲動
  await slowScroll(page, '#v-health .protect-body', 400, 2800);
  await sleep(600);

  // ── S3: 點 Kaleidoscope → AI chat → 停留 3 秒 → 捲到底 → 停留 2 秒 ────────
  console.log('S3: Tap Kaleidoscope nav → AI chat → 3s pause → scroll to bottom → 2s');
  await tapAndNav(page, '#nav-ai', 2);
  await sleep(600);
  await sleep(2000);  // 停留 2 秒後開始捲動
  await slowScroll(page, '#v-ai .chat-msgs', 9999, 2000);
  await sleep(2000);

  // ── S4: 回 Home → 停留 2 秒 → 點 Yuki 頭像 → Detail → Growth Report ─────────
  console.log('S4: Tap Home → 2s pause → tap Yuki avatar → Growth Report');
  await tapAndNav(page, '#nav-0', 0);
  await sleep(600);
  await resetScroll(page, '#v-home .view-scroll');
  await sleep(2000);

  // 找 constellation 裡的 Yuki 節點，顯示 ripple → 跳 Detail view
  const yukiBox = await page.evaluate(() => {
    const nodes = document.querySelectorAll('g.node');
    for (const n of nodes) {
      if (n.getAttribute('onclick')?.includes("'yuki'")) {
        return n.getBoundingClientRect().toJSON();
      }
    }
    return null;
  });
  if (yukiBox) {
    await showRipple(page, Math.round(yukiBox.x + yukiBox.width / 2), Math.round(yukiBox.y + yukiBox.height / 2));
  }
  await sleep(450);
  await page.evaluate(() => showDetail('yuki'));
  await sleep(800);

  // 點 "View growth report" 主按鈕 → v-yuki (switchView(6))
  await tapAndNav(page, '.action-btn.primary', 6);
  await sleep(600);

  // ── S5: Yuki's report → 停留 3 秒 → 慢速捲動 → 停留 3 秒 → 回 Home ──────────
  // → 重置 → 停留 3 秒 → 捲動 → 點 Protection → Safety report
  console.log('S5: 3s pause → Yuki report scroll → 3s pause → Home → 3s pause → scroll → tap Protection → Safety');
  await sleep(2000);  // 停留 2 秒後開始捲動
  await slowScroll(page, '#v-yuki .protect-body', 350, 2500);
  await sleep(2000);
  await tapAndNav(page, '#nav-0', 0);
  await sleep(600);
  await resetScroll(page, '#v-home .view-scroll');
  await sleep(2000);  // 停留 2 秒後開始捲動
  await slowScroll(page, '#v-home .view-scroll', 480, 2500);
  await sleep(400);
  await tapAndNav(page, '.bento-card.protect', 7);
  await sleep(600);
  await sleep(2000);  // 停留 2 秒後開始捲動
  await slowScroll(page, '#v-safety .protect-body', 280, 2200);
  await sleep(600);

  // ── 結束 ──────────────────────────────────────────────────────────────────────
  const videoPath = await page.video().path();
  await context.close();
  await browser.close();

  console.log('\n✅ 錄影完成！');
  console.log('輸出路徑:', videoPath);
})();
