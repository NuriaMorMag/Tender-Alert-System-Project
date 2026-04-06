# --------------------------------------------------
# FUNCTION: analyze_tender
# --------------------------------------------------
# This function checks if a tender matches a company.
#
# CURRENT LOGIC:
# - Very simple keyword matching
#
# FUTURE:
# - Replace with AI (Gemini, OpenAI, etc.)
# --------------------------------------------------
def analyze_tender(company, tender):
    # Convert text to lowercase for easier comparison
    company_text = company["description"].lower()
    tender_text = tender["description"].lower()

    # Split company description into words
    words = company_text.split()

    # Check if any word appears in the tender description
    for word in words:
        if word in tender_text:
            return True  # Match found

    return False  # No match

# --------------------------------------------------
# FUTURE AI INTEGRATION
# --------------------------------------------------
# This is where real AI would go
#
# Example idea:
# - Send company + tender text to Gemini
# - Ask: "Is this relevant?"
# - Get a score (0–1)
#
# def analyze_with_ai(company, tender):
#     pass