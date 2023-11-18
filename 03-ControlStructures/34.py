amount = int(input("Enter the amount in PLN: "))

fives = amount // 5

amount = amount % 5

twos = amount // 2

amount = amount % 2

ones = amount // 1

print(f"5 zl: {fives}")
print(f"2 zl: {twos}")
print(f"1 zl: {ones}")
