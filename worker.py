# worker.py

import time

from tender_fetch_playwright import fetch_tenders

from database_helper import (
    get_users,
    save_tender_if_new
)

from coincidence_analyzer import is_relevant

from email_sender import send_email

from time_classifier import classify_by_recency


def run():

    while True:

        print("Checking tenders...")

        try:

            tenders = fetch_tenders()

            users = get_users()

            print(f"Fetched: {len(tenders)}")

            for tender in tenders:

                full_text = f"""
                {tender["procurement_name"]}
                {tender["contracting_authority"]}
                {tender["cpv"]}
                """

                print("CHECKING:", full_text)

                # CHECK KEYWORDS
                if is_relevant(full_text):

                    print("RELEVANT TENDER FOUND!")

                    is_new = save_tender_if_new(tender)

                    if is_new:

                        category = classify_by_recency(
                            tender["publication_date"]
                        )

                        print(f"""
NEW RELEVANT TENDER
CATEGORY: {category}
TITLE: {tender["procurement_name"]}
DATE: {tender["publication_date"]}
""")

                        for email in users:

                            send_email(
                                email,
                                f"""
[{category.upper()} TENDER]

TITLE:
{tender["procurement_name"]}

PUBLICATION DATE:
{tender["publication_date"]}

DEADLINE:
{tender["submission_deadline"]}

CPV:
{tender["cpv"]}
"""
                            )

        except Exception as e:

            print(e)

        # Every 6 hours
        time.sleep(21600)


if __name__ == "__main__":
    run()