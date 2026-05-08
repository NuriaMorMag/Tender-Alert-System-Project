# worker.py - AUTOMATION ENGINE

import time
from tender_fetch_playwright import fetch_tenders
from database_helper import get_users, save_tender_if_new
from coincidence_analyzer import is_relevant
from email_sender import send_email
from time_classifier import classify_by_recency

from datetime import datetime


from datetime import datetime

def parse_date(date_str):
    if not date_str:
        return None

    # 1) Formato ISO (2026-05-18T12:00:00)
    try:
        return datetime.fromisoformat(date_str)
    except:
        pass

    # 2) Formato tipo 18.05.2026
    try:
        return datetime.strptime(date_str, "%d.%m.%Y")
    except:
        pass

    # 3) Formato tipo 18-05-2026
    try:
        return datetime.strptime(date_str, "%d-%m-%Y")
    except:
        pass

    # 4) Formato tipo 18/05/2026
    try:
        return datetime.strptime(date_str, "%d/%m/%Y")
    except:
        pass

    return None


def run():

    while True:
        print("Checking for new tenders...")

        try:
            tenders = fetch_tenders()
            print("RAW TENDERS:", tenders[:5])

            # filtrar fechas válidas
            tenders = [t for t in tenders if parse_date(t["date"])]

            # ordenar por fecha de publicación
            tenders.sort(key=lambda x: parse_date(x["date"]), reverse=True)

            users = get_users()

            for tender in tenders:
                text = tender["text"]
                date_str = tender["date"]

                published_date = parse_date(date_str)

                if not published_date:
                    continue

                # relevancia
                if is_relevant(text):

                    is_new = save_tender_if_new(text, date_str)

                    category = classify_by_recency(published_date)

                    if is_new:
                        for email in users:
                            send_email(email, f"[{category.upper()}] {text}")

        except Exception as e:
            print(f"Error in worker: {e}")

        time.sleep(21600)


if __name__ == "__main__":
    run()