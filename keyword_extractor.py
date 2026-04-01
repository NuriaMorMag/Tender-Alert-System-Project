# Extract keywords from company description
def extract_keywords(description):
    # Convert text to lowercase and split into words
    words = description.lower().split()

    # Remove duplicates using set
    keywords = list(set(words))

    return keywords