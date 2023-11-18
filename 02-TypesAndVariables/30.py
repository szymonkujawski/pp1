import random
dice_number = random.randint(1,6)

if dice_number==1 or dice_number==6:
    print(f"Dice rolled: {dice_number}")
    print(f"Special number: True")
else:
    print(f"Dice rolled: {dice_number}")
    print(f"Special number: False")