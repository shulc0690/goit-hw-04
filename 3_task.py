import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]


def normalize_phone(number: str) -> str:
    cleaned_number = re.sub(r'[^\d+]', '', number)    
    if not cleaned_number.startswith('+'):
        # Додаємо пробіли там де не вистачає цифр. наприклад '671234567' -> '    671234567'
        cleaned_number = f"{int(cleaned_number):13d}"
        # Замінуємо пробіли на потрібні цифри та +
        if cleaned_number[0] == ' ':
            cleaned_number = cleaned_number.replace(' ', '+', 1)
        if cleaned_number[1] == ' ':
            cleaned_number = cleaned_number.replace(' ', '3', 1)
        if cleaned_number[2] == ' ':
            cleaned_number = cleaned_number.replace(' ', '8', 1)
        if cleaned_number[3] == ' ':
            cleaned_number = cleaned_number.replace(' ', '0', 1)
    return cleaned_number

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)