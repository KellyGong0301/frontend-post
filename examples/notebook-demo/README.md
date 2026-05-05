# Notebook Demo

A 7-card carousel in the **校园手账 Campus Notebook** style — this is the actual deck that announces this skill (cover, pain points, intro, 12-style preview, usage, design principles, open-source declaration).

**渲染好的成品图**：见仓库根目录 [`docs/preview/`](../../docs/preview/)。

## Run it locally

### 1. Open the HTML in a browser

```bash
open index.html
```

You'll see all 7 cards stacked vertically (each scaled to 360×480 for screen preview, real size is 1080×1440).

### 2. Export to PNG

From this directory:

```bash
npm init -y && npm install puppeteer-core
node ../../scripts/render.js index.html png_output
```

You'll get `png_output/card_01.png` … `card_07.png` at 2160×2880 (retina 2x).

Requires:
- Node.js
- Google Chrome installed at `/Applications/Google Chrome.app/...` (macOS default)

For other platforms or if you don't have Chrome, use the Python version:

```bash
pip install playwright && playwright install chromium
python ../../scripts/render.py index.html png_output
```

## Customize the style

All theme variables are in `:root` at the top of `<style>`:

```css
:root {
  --bg: #FDFBF5;          /* 米黄纸 */
  --ink: #2C2826;         /* 黑色字 */
  --ink-pen: #2A4D8F;     /* 钢笔蓝 */
  --highlight: #FFE066;   /* 荧光黄 */
  --accent: #E84855;      /* 红笔 */
  --font-display: "LXGW WenKai", serif;
  --font-hand: "Long Cang", cursive;
}
```

Change these and re-run the render command — the entire deck rethemes.

For all 12 preset palettes, see [`references/STYLE_PRESETS.md`](../../references/STYLE_PRESETS.md).
