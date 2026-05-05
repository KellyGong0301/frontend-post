#!/usr/bin/env python3
"""
Render each .card in an HTML deck to a 1080×1440 (or 1080×1080) PNG.

Usage:
    python render.py path/to/index.html [output_dir]

Default output dir: ./png_output

Requires:
    pip install playwright
    playwright install chromium
"""

from __future__ import annotations
import sys
import pathlib

try:
    from playwright.sync_api import sync_playwright
except ImportError:
    print("ERROR: playwright not installed.")
    print("Run:  pip install playwright && playwright install chromium")
    sys.exit(1)


def render(html_path: pathlib.Path, out_dir: pathlib.Path) -> None:
    out_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch()
        # Big viewport so the unscaled card fits; 2x DPR for crisp text.
        page = browser.new_page(
            viewport={"width": 1200, "height": 1600},
            device_scale_factor=2,
        )
        page.goto(f"file://{html_path}")

        # Disable preview-only scaling so screenshots capture the real 1080×1440.
        page.add_style_tag(content="""
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
        """)
        # Wait briefly for fonts (Google Fonts) to settle.
        page.wait_for_load_state("networkidle")
        page.wait_for_timeout(500)

        cards = page.query_selector_all(".card")
        if not cards:
            print("ERROR: no .card elements found in HTML.")
            sys.exit(2)

        print(f"Found {len(cards)} cards. Rendering to {out_dir}/")
        for i, card in enumerate(cards, start=1):
            path = out_dir / f"card_{i:02d}.png"
            card.screenshot(path=str(path), omit_background=False)
            print(f"  ✓ {path.name}")

        browser.close()
        print(f"\nDone. {len(cards)} PNGs saved to {out_dir.resolve()}")


def main() -> None:
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(1)

    html_path = pathlib.Path(sys.argv[1]).resolve()
    if not html_path.exists():
        print(f"ERROR: {html_path} not found")
        sys.exit(1)

    out_dir = pathlib.Path(sys.argv[2]).resolve() if len(sys.argv) > 2 \
              else pathlib.Path.cwd() / "png_output"

    render(html_path, out_dir)


if __name__ == "__main__":
    main()
