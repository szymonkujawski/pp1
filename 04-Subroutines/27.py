def f(card_number):
    first_2 = card_number[:2]
    last_4 = card_number[-4:]
    combined = first_2 + 10*"*" + last_4
    return combined

card_number = "5290312400019022"

result = f(card_number)

print(result)