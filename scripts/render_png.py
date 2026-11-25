"""html/*.html → png/*.png

用無頭瀏覽器把 HTML 圖卡截成 1080×1350 的 PNG（2 倍解析度）。
安裝：pip install playwright && playwright install chromium
用法：python scripts/render_png.py
"""
import sys
from pathlib import Path
from playwright.sync_api import sync_playwright

ROOT = Path(__file__).resolve().parent.parent


def main():
    files = [Path(a) for a in sys.argv[1:]] or sorted((ROOT / "html").glob("*.html"))
    with sync_playwright() as p:
        try:
            browser = p.chromium.launch()
        except Exception:
            browser = p.chromium.launch(channel="chrome")  # 沒裝 playwright chromium 時改用本機 Chrome
        page = browser.new_page(viewport={"width": 1080, "height": 1350}, device_scale_factor=2)
        for f in files:
            f = f if f.is_absolute() else ROOT / f
            page.goto(f.as_uri())
            page.wait_for_timeout(800)  # 等字型載入
            out = ROOT / "png" / (f.stem + ".png")
            page.screenshot(path=str(out))
            print("✓", out.relative_to(ROOT))
        browser.close()


if __name__ == "__main__":
    main()
