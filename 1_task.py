from datetime import datetime

def get_days_from_today(date: str) -> int:
    try:
        input_date = datetime.strptime(date, "%Y-%m-%d")
        current_date = datetime.today()
        return (current_date - input_date).days
    except ValueError:
        return 'Input data is not correct. Use \'YYYY-MM-DD\''

print(get_days_from_today("2021-10-09"))