from datetime import datetime

def get_days_from_today(date):
    today = datetime.now()
    return (today - date).days


date = datetime(2020, 10, 9).center(100)
print(f"-{get_days_from_today(date)}")
