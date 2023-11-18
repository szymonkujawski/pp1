def f(amount_to_pay):
    fives = amount_to_pay//5
    amount_to_pay = amount_to_pay%5
    twos = amount_to_pay//2
    amount_to_pay = amount_to_pay%2
    ones = amount_to_pay//1
    amount_to_pay = amount_to_pay%1
    all = fives + twos + ones
    return all

amount = int(input("Enter amount to pay: "))

print(f"To pay {amount} you have to use {f(amount)} coins")



