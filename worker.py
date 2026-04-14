# worker.py - AUTOMATION ENGINE

import time
from tender_fetch_playwright import fetch_tenders
from database_helper import get_users, save_tender_if_new
from coincidence_analyzer import is_relevant
from email_sender import send_email


def run():
    """
    Main loop that runs forever and checks for new tenders.
    """

    while True:
        print("Checking for new tenders...")

        try:
            tenders = fetch_tenders()
            users = get_users()

            for tender in tenders:
                text = tender["text"]

                # Check if tender is relevant
                if is_relevant(text):

                    # Avoid duplicates
                    if save_tender_if_new(text):

                        for email in users:
                            print(f"Sending alert to {email}")
                            send_email(email, text)

        except Exception as e:
            print(f"Error in worker: {e}")

        # Wait 6 hours (21600 seconds)
        time.sleep(21600)


if __name__ == "__main__":
    run()