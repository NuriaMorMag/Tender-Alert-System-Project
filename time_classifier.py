from datetime import datetime, timedelta

def classify_by_recency(published_date):
    """
    Classify tender based on publication date.
    """

    now = datetime.now()
    diff = now - published_date

    if diff <= timedelta(days=1):
        return "new"

    elif diff <= timedelta(days=7):
        return "recent"

    else:
        return "old"