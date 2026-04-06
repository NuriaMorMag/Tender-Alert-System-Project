# jnportal_fetch.py
import requests
from bs4 import BeautifulSoup
from datetime import datetime

BASE_URL = "https://jnportal.ujn.gov.rs"


def fetch_new_tenders():
    """
    Fetch new tenders from jnportal.ujn.gov.rs.

    REAL WORLD:
    - Inspect the HTML of the tenders list page.
    - Find the correct CSS selectors for each tender item.
    - For each tender:
      * title
      * link
      * short description (if available)
      * date

    HERE:
    - We show the structure and example logic.
    - You must adapt 'soup.select(...)' to the real HTML.
    """
    list_url = BASE_URL  # or a specific path if needed
    response = requests.get(list_url, timeout=15)
    response.raise_for_status()

    soup = BeautifulSoup(response.text, "html.parser")
    tenders = []

    # TODO: change this selector to match real tender items
    # Example: each tender might be in a <div class="tender-row"> or similar
    for item in soup.select("a.tender-link"):
        title = item.get_text(strip=True)
        href = item.get("href")

        if not href:
            continue

        # Build full URL if it's relative
        if href.startswith("/"):
            tender_url = BASE_URL + href
        else:
            tender_url = href

        # Optionally, fetch tender detail page for more text
        description = fetch_tender_detail(tender_url)

        tenders.append(
            {
                "title": title,
                "description": description,
                "url": tender_url,
                "published_at": datetime.utcnow().isoformat(),
            }
        )

    return tenders


def fetch_tender_detail(url: str) -> str:
    """
    Fetch and extract text from a single tender detail page.
    """
    try:
        response = requests.get(url, timeout=15)
        response.raise_for_status()
    except Exception:
        return ""

    soup = BeautifulSoup(response.text, "html.parser")

    # TODO: adjust this to real structure (e.g. main content div)
    texts = [p.get_text(strip=True) for p in soup.find_all("p")]
    return " ".join(texts)