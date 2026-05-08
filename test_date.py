from worker import parse_date

dates = [
    "2026-05-18T12:00:00",
    "2026-01-01T00:00:00"
]

for d in dates:
    print(d, "->", parse_date(d))