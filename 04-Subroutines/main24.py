import check

number = int(input("Enter number: "))
x_range = 2
y_range = 15

result = check.in_range(number, x_range, y_range)

print(f"Number {number} in the range <{x_range},{y_range}>: {result}")

