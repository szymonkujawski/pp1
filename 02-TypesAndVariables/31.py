import random
dice_number = random.randint(1,6)

user_guess = int(input("Wprowadz numer od 1 do 6: "))

if dice_number==user_guess:
    print(f"Twoja liczba: {user_guess}, wylosowana liczba: {dice_number}. Wygrales!")
else:
     print(f"Twoja liczba: {user_guess}, wylosowana liczba: {dice_number}. Niestery tym razem sie nie udalo!")