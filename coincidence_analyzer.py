# Calculate how well a tender matches a company
def calculate_match(company_keywords, tender_text):
    score = 0

    # Check if each keyword appears in the tender text
    for word in company_keywords:
        if word in tender_text.lower():
            score += 10  # increase score for each match

    # Limit score to 100
    return min(score, 100)