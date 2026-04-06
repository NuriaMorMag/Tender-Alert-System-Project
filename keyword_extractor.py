# keyword_extractor.py

def generate_keywords(profile_text: str) -> str:
    """
    Generate search keywords from company profile.

    REAL WORLD:
    - You would send profile_text to Google Gemini API.
    - Gemini would return a list of smart keywords like:
      ["smart card", "RFID card", "access control system"]

    HERE:
    - We keep it simple: split into words, remove duplicates.
    - This is a placeholder where you can plug real AI later.
    """
    text = profile_text.lower().replace(",", " ").replace(".", " ")
    words = text.split()
    unique_words = sorted(set(words))
    return ",".join(unique_words)