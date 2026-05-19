# time_classifier.py

from datetime import datetime


def classify_by_recency(publication_date):

    # Convert string to datetime
    publication_date = datetime.strptime(
        publication_date,
        "%d.%m.%Y"
    )

    now = datetime.now()

    diff = now - publication_date

    days = diff.days

    if days <= 1:
        return "new"

    elif days <= 7:
        return "recent"

    else:
        return "old"