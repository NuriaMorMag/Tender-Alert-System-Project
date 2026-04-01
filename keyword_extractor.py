# Extract keywords from company description
def extract_keywords(description):
    # Convert text to lowercase
    words = description.lower().split()

    # Remove duplicates using set
    unique_words = list(set(words))

    return unique_words