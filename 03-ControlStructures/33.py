decimal_number = int(input("Enter decimal number: "))
decimal_number_additional = decimal_number

binary_number = str('')

while decimal_number > 0:
    remainder = decimal_number % 2
    binary_number = str(remainder) + str(binary_number)
    decimal_number = decimal_number // 2

print(f"Decimal : {decimal_number_additional}, binary: {binary_number}")