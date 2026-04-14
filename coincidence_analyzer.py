# coincidence_analyzer.py

# Keywords to match tenders
KEYWORDS = ["smartcards", "javacards"]


def is_relevant(tender_text):
    """
    Check if a tender contains any relevant keyword.
    """

    text = tender_text.lower()

    for keyword in KEYWORDS:
        if keyword in text:
            return True

    return False