from coincidence_analyzer import calculate_match

# Simulated tenders (instead of real TED API)
def get_fake_tenders():
    return [
        "Looking for smart card suppliers",
        "Need construction company",
        "RFID card system project"
    ]

# Check tenders against company keywords
def check_tenders(keywords):
    tenders = get_fake_tenders()

    for tender in tenders:
        score = calculate_match(keywords, tender)

        # If score is high enough → alert
        if score >= 20:
            print(f"[ALERT] Match found: {tender} ({score}%)")