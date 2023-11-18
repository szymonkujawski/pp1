import mymath

your_number = int(input("Enter your number <1,9>: "))
computer_number = mymath.generate_number()

if your_number==computer_number:
    print(f"Your number is: {your_number}, computer number is: {computer_number}. YOU WON!!!")
else:
    print(f"Your number is: {your_number}, computer number is: {computer_number}. YOU LOST!!!")