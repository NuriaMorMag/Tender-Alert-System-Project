# coincidence_analyzer.py

KEYWORDS = [
    "smartcard",
    "smartcards",
    "javacard",
    "javacards",
    "систем",
    "card"
]  


def is_relevant(text):
    """
    Check if a tender contains any relevant keyword.
    """
    text = text.lower()

    for keyword in KEYWORDS:

        if keyword in text:
            return True

    return False