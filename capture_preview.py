"""
capture_preview.py
------------------
Takes a full-page screenshot of dashboard.html → preview.png
Also crops and saves the first chart area → preview_chart1.png

Requirements:
    pip install playwright
    playwright install chromium
"""

import asyncio
import os
from pathlib import Path
from playwright.async_api import async_playwright


DASHBOARD_PATH = Path(__file__).parent / "dashboard.html"
OUTPUT_FULL    = Path(__file__).parent / "preview.png"
OUTPUT_CHART1  = Path(__file__).parent / "preview_chart1.png"

# How long to wait (ms) for Plotly charts to fully render before screenshotting
RENDER_WAIT_MS = 2500


async def capture():
    if not DASHBOARD_PATH.exists():
        print("[ERROR] dashboard.html not found. Run generar_dashboard.py first.")
        return

    file_url = DASHBOARD_PATH.as_uri()
    print(f"Opening  -> {file_url}")

    async with async_playwright() as p:
        browser = await p.chromium.launch(headless=True)
        page = await browser.new_page(viewport={"width": 1400, "height": 900})

        # Navigate and wait for network + Plotly render
        await page.goto(file_url, wait_until="networkidle")
        await page.wait_for_timeout(RENDER_WAIT_MS)

        # ── 1. Full-page screenshot ─────────────────────────────────────────
        await page.screenshot(path=str(OUTPUT_FULL), full_page=True)
        print(f"[OK] Full screenshot saved -> {OUTPUT_FULL.name}")

        # ── 2. Cropped: first .chart-card element ───────────────────────────
        first_chart = page.locator(".chart-card").first
        await first_chart.screenshot(path=str(OUTPUT_CHART1))
        print(f"[OK] Chart-1 crop saved   -> {OUTPUT_CHART1.name}")

        await browser.close()

    print("\nDone! Files written to:", DASHBOARD_PATH.parent)


if __name__ == "__main__":
    asyncio.run(capture())
