from datetime import datetime

def get_days_from_today(date_str):
    try:
        date = datetime.strptime(date_str, "%Y-%m-%d").date()
        today = datetime.today().date()
        return (today - date).days
    except ValueError:
        return None

date_str = input("Попрошу вводить таким образом 🙃 YYYY-MM-DD: ")
days = get_days_from_today(date_str)

if days is None:
    print("Некорректные данные")
else:
    print(f"-{days}")