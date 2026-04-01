# Compare keywords with tender text and give a score
def match_score(keywords, tender_text):
    score = 0

    # Check if each keyword appears in the tender
    for word in keywords:
        if word in tender_text.lower():
            score += 10  # Add points if match found

    # Limit score to maximum 100
    return min(score, 100)