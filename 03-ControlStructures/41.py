pin = "0805"

attempt = 0

while attempt < 3:
    enter_pin = input("Enter the PIN code: ")

    if enter_pin==pin:
        print("Correct!")
        break
    else:
        print("Incorrect...")
        attempt += 1

if attempt == 3:
    print("Sorry, your payment card has been blocked.")
