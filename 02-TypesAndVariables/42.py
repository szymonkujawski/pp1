binary_number = str(input("Enter binary number: "))

decimal_number = 0

if binary_number[0]=="1":
    decimal_number = decimal_number+8
else:
    decimal_number = decimal_number+0

if binary_number[1]=="1":
    decimal_number = decimal_number+4
else:
    decimal_number = decimal_number+0

if binary_number[2]=="1":
    decimal_number = decimal_number+2
else:
    decimal_number = decimal_number+0

if binary_number[3]=="1":
    decimal_number = decimal_number+1
else:
    decimal_number = decimal_number+0

print(f"Binary number in decimal notation: {decimal_number}")