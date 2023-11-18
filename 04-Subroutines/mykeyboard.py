def read_number():
    return int(input("Enter number: "))

if __name__ == "__main__":
    number1 = read_number()
    number2 = read_number()
    sum = number1 + number2
    print(f"{sum}")
