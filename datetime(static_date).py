from datetime import datetime

def get_days_from_today(date):
    today = datetime.now()
    return (today - date).days


date_str = input("Попрошу вводить таким образом 🙃 YYYY-MM-DD: ")
date = datetime.strptime(date_str, "%Y-%m-%d")
print(f"-{get_days_from_today(date)}")

