# tender_fetch_playwright.py

from playwright.sync_api import sync_playwright


def fetch_tenders():
    """
    Open the Serbian procurement portal and extract tenders.
    """

    tenders = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        # Open website
        page.goto("https://jnportal.ujn.gov.rs/konzola", timeout=60000)

        # Wait for table to load (better than sleep)
        page.wait_for_selector("table")

        rows = page.query_selector_all("table tr")

        for row in rows:
            text = row.inner_text().strip()

            if text:
                tenders.append({
                    "text": text
                })

        browser.close()

    return tenders