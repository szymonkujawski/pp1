number = int(input("Enter number: ")) 
quantity = 0
sum = 0
mean = 0

while number != 0:
    quantity += 1
    sum = sum + number
    number = int(input("Enter number: ")) 

print(f"Quantity={quantity}, Sum={sum}, Mean={sum/quantity}")