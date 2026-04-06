# website_analyzer.py
import requests
from bs4 import BeautifulSoup

def analyze_website(url: str) -> str:
    """
    Download and extract text from the company website.

    REAL WORLD:
    - Crawl multiple pages
    - Clean boilerplate
    - Send text to AI to understand the business

    HERE:
    - Download only the homepage
    - Extract text from <p> tags
    """
    if not url:
        return ""

    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
    except Exception:
        return ""

    soup = BeautifulSoup(response.text, "html.parser")
    paragraphs = [p.get_text(strip=True) for p in soup.find_all("p")]
    return " ".join(paragraphs)