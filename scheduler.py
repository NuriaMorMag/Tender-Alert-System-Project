# scheduler.py - Run matching every X hours
from database_helper import get_active_companies
from coincidence_analyzer import compute_match_score
from email_verification import send_email
from tender_fetch import fetch_new_tenders

def run_matching_cycle():
    """
    Main logic:
    1. Get all active companies (verified and not unsubscribed)
    2. Fetch new tenders from jnportal
    3. For each company and each tender:
       - compute match score
       - if score >= 20, send email alert
    """
    companies = get_active_companies()
    tenders = fetch_new_tenders()

    if not companies or not tenders:
        print("No companies or no tenders to process.")
        return

    for company in companies:
        profile_text = company["description"] + " " + (company["keywords"] or "")

        for tender in tenders:
            score = compute_match_score(profile_text, tender["description"])

            if score >= 20:
                subject = f"Tender match: {tender['title']}"
                body = (
                    f"Hello {company['name']},\n\n"
                    f"We found a public tender that may match your business.\n\n"
                    f"Title: {tender['title']}\n"
                    f"URL: {tender['url']}\n"
                    f"Match score: {score}%\n\n"
                    f"If you no longer want to receive these emails, you can unsubscribe.\n"
                )

                print(f"[DEBUG] Would send email to {company['email']} with score {score}")
                # In production, uncomment:
                # send_email(company["email"], subject, body)

if __name__ == "__main__":
    # This file would be called by a scheduler (cron, Cloud Scheduler, etc.)
    run_matching_cycle()