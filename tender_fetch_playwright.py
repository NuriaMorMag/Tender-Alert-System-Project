from playwright.sync_api import sync_playwright

def fetch_tenders():
    url = "https://jnportal.ujn.gov.rs/"

    tenders = []

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()

        page.goto(url)
        page.wait_for_timeout(5000)

        rows = page.query_selector_all("table tbody tr")

        for row in rows:
            cols = row.query_selector_all("td")

            if len(cols) >= 2:
                text = cols[0].inner_text().strip()
                date = cols[1].inner_text().strip()

                tenders.append({
                    "text": text,
                    "date": date
                })

        browser.close()

    return tenders