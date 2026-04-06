# coincidence_analyzer.py

def compute_match_score(company_profile: str, tender_text: str) -> int:
    """
    Compute how well a tender matches a company (0–100).

    REAL WORLD:
    - Send both texts to Google Gemini:
      "Given this company profile and this tender, how relevant is it (0-100)?"
    - Parse the numeric score from the AI response.

    HERE:
    - Simple placeholder:
      * split company_profile into words
      * count how many appear in tender_text
      * convert to percentage
    """
    if not company_profile:
        return 0

    tender_text = tender_text.lower()
    words = company_profile.lower().split()
    words = [w for w in words if len(w) > 3]  # ignore very short words

    if not words:
        return 0

    matches = 0
    for w in set(words):
        if w in tender_text:
            matches += 1

    score = int((matches / len(set(words))) * 100)
    return score