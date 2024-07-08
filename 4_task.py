from datetime import datetime

users = [
    {"name": "John Doe", "birthday": "1985.07.15"},
    {"name": "Jane Smith", "birthday": "1990.07.08"},
    {"name": "Jane Smith 2", "birthday": "1990.06.12"}
]

def get_upcoming_birthdays(users: list[dict]) -> list[dict]:
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        try:
            birthday = datetime.strptime(user['birthday'],'%Y.%m.%d').date()
        except ValueError:
            return f'{user['name']} має некоректну дату.'
        
        birthday_this_year  = birthday.replace(year = today.year)
        if birthday_this_year < today:
            continue
        diff_in_days = (birthday_this_year - today).days
        if diff_in_days <= 7 and ['0','6'].count(birthday_this_year.strftime('%w')) == 0:# в моїй системі 0-Неділя
            upcoming_birthdays.append({'name': user['name'], 'congratulation_date': birthday_this_year.strftime('%Y.%m.%d')})
    return upcoming_birthdays


upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)