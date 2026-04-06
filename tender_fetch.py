import time
from coincidence_analyzer import analyze_tender
from database_helper import save_tender, get_all_companies
from email_verification import send_email


# --------------------------------------------------
# FUNCTION: fetch_tenders
# --------------------------------------------------
# This function is responsible for getting tenders.
#
# Right now, this is a SIMULATION.
# NOT connecting to the real Serbian website.
#
# In a real system:
# - We would send a request to the website
# - Download the HTML page
# - Extract data (titles, descriptions, links)
#
# Example tools (NOT used here):
# - requests (to download the page)
# - BeautifulSoup (to parse HTML)
# --------------------------------------------------
def fetch_tenders():
    print("Fetching tenders (simulated)...")

    # Simulated data (acts like scraped data)
    # Each item represents one tender from the website
    tenders = [
        {
            "title": "IT Services for Government",
            "description": "Looking for a software development company",
            "link": "https://example.com/tender1"
        },
        {
            "title": "Construction Project",
            "description": "Road construction services needed",
            "link": "https://example.com/tender2"
        }
    ]

    # Return list of tenders
    return tenders


# --------------------------------------------------
# FUNCTION: process_tenders
# --------------------------------------------------
# This is the MAIN LOGIC of the system.
#
# Steps:
# 1. Get tenders
# 2. Get all companies
# 3. Compare each tender with each company
# 4. If match → send email
# --------------------------------------------------
def process_tenders():
    print("Starting tender processing...")

    # Step 1: get tenders (simulated)
    tenders = fetch_tenders()

    # Step 2: get companies from database
    companies = get_all_companies()

    # Loop through each tender
    for tender in tenders:
        print(f"Processing tender: {tender['title']}")

        # Save tender to database
        save_tender(tender)

        # Compare with each company
        for company in companies:
            print(f"Checking company: {company['email']}")

            # Step 3: analyze match
            match = analyze_tender(company, tender)

            # Step 4: if match → notify
            if match:
                print("Match found!")

                send_email(
                    to=company["email"],
                    subject="New Tender Match",
                    body=f"A relevant tender was found: {tender['title']}"
                )
            else:
                print("No match.")


# --------------------------------------------------
# AUTOMATION LOOP
# --------------------------------------------------
# This simulates running the system automatically.
#
# In real life:
# - We would use cron jobs or cloud schedulers
# - Example: run every 8 hours
# --------------------------------------------------
if __name__ == "__main__":
    while True:
        process_tenders()

        print("Waiting 8 hours before next run...")
        time.sleep(60 * 60 * 8)