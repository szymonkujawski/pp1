def count_letters(text, letter):
    count = 0
    for char in text:
        if char==letter:
            count += 1
    return count


text = "You never get a second chance to make a first impression"

letter = "e"

result = count_letters(text, letter)

print(f"Ilosc litery 'e' w tekscie: {result}")