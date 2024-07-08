import random

def get_numbers_ticket(min: int, max: int, quantity: int)  -> list:
    try:
        if min < 1 or max > 1000 or quantity < min or quantity > max:
            return []    
        numbers = random.choices(range(min, max), k=quantity)
        numbers.sort()
        return numbers
    except TypeError:
        return 'Вхідні данні повинні буди числами.'

lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)