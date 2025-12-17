import random

def get_numbers_ticket(min, max, quantity):
    if min < 1 or max > 1000:
        return 
    if quantity > (max - min + 1):
        return 
    return sorted(random.sample(range(min, max + 1), quantity))

min = int(input("min: "))
max = int(input("max: "))
quantity = int(input("quantity: "))

print(get_numbers_ticket(min, max, quantity))