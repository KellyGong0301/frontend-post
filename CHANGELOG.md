# Changelog

All notable changes to **frontend-post** will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.1.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [0.1.0] — 2026-05-05

### Initial public release

#### Added
- **`SKILL.md`** — main skill flow with 6 phases (mode detection, content discovery, style discovery, generation, quality self-check, delivery).
- **12 curated style presets** — 奶油拿铁 / 莫兰迪 / 多巴胺 / 校园手账 / 极简黑白 / 港风胶片 / 杂志大字 / 暗黑科技 / 国风水墨 / 日系治愈 / 复古杂志 / 咖啡店黑板. Full color / font / decoration spec in `references/STYLE_PRESETS.md`.
- **9 cover-headline hook formulas** — number, contrast, question, self-disclosure, warning, freebie, story, anti-cliché, identity. See `references/HOOK_PATTERNS.md`.
- **Two render scripts**:
  - `scripts/render.js` — Node + puppeteer-core, reuses system Chrome, zero extra download
  - `scripts/render.py` — Python + Playwright, cross-platform stable
- **Hard constraints** — fixed 1080×1440 / 1080×1080 pixels, content density caps per card type, mandatory Chinese typography (Noto Serif SC / LXGW WenKai / Ma Shan Zheng / ZCOOL series), banned generic-AI aesthetics (purple gradients, default Inter/system fonts).
- **`examples/notebook-demo/`** — 7-card 校园手账 deck announcing the skill itself, fully runnable.
- **`docs/preview/`** — rendered PNG previews of the demo deck.
- MIT license, comprehensive `.gitignore`, bilingual README.

#### Design philosophy
- **Layout tool, not content generator** — users provide text + style preferences; AI just executes.
- **Strong constraints over creative freedom** — adapts the [frontend-slides](https://github.com/zarazhangrui/frontend-slides) approach: density limits + curated presets + banned-pattern list = no generic AI look.
- **User control surface** — all theme tokens (`--bg`, `--ink`, `--accent`, `--font-display`, `--font-body`) exposed in `:root` for live editing.

[0.1.0]: https://github.com/KellyGong0301/frontend-post/releases/tag/v0.1.0
