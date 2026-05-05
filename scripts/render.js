/**
 * Render each .card in an HTML deck to a 1080×1440 PNG.
 *
 * Usage: node scripts/render.js [html_path] [out_dir]
 * Defaults: index.html → png_output/
 *
 * Uses system Chrome via puppeteer-core (no extra download).
 */

const puppeteer = require('puppeteer-core');
const path = require('path');
const fs = require('fs');

const CHROME_PATH = '/Applications/Google Chrome.app/Contents/MacOS/Google Chrome';

(async () => {
  const htmlArg = process.argv[2] || 'index.html';
  const outArg  = process.argv[3] || 'png_output';

  const htmlPath = path.resolve(htmlArg);
  const outDir   = path.resolve(outArg);

  if (!fs.existsSync(htmlPath)) {
    console.error(`ERROR: ${htmlPath} not found`);
    process.exit(1);
  }
  fs.mkdirSync(outDir, { recursive: true });

  const browser = await puppeteer.launch({
    executablePath: CHROME_PATH,
    headless: 'new',
  });
  const page = await browser.newPage();
  await page.setViewport({ width: 1200, height: 1600, deviceScaleFactor: 2 });

  await page.goto('file://' + htmlPath, { waitUntil: 'networkidle0' });

  // Disable preview-only scaling so the real 1080×1440 card is captured.
  await page.addStyleTag({
    content: `
      html, body { background: #fff !important; padding: 0 !important; margin: 0 !important; }
      .deck { gap: 0 !important; padding: 0 !important; }
      .card-wrap {
        width: 1080px !important;
        height: auto !important;
        aspect-ratio: auto !important;
        box-shadow: none !important;
        border-radius: 0 !important;
        overflow: visible !important;
      }
      .card { transform: none !important; }
    `,
  });

  // Wait for web fonts to settle.
  await page.evaluate(() => document.fonts.ready);
  await new Promise(r => setTimeout(r, 1500));

  const cards = await page.$$('.card');
  if (cards.length === 0) {
    console.error('ERROR: no .card elements found.');
    await browser.close();
    process.exit(2);
  }

  console.log(`Found ${cards.length} cards. Rendering to ${outDir}/`);
  for (let i = 0; i < cards.length; i++) {
    const filename = path.join(outDir, `card_${String(i + 1).padStart(2, '0')}.png`);
    await cards[i].screenshot({ path: filename, omitBackground: false });
    console.log(`  ✓ ${path.basename(filename)}`);
  }

  await browser.close();
  console.log(`\nDone. ${cards.length} PNGs saved to ${outDir}`);
})();
