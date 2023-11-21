import random
list = [random.randint(0,999) for i in range(8)]

print("-", end="")
print("-----"*8)
for element in list:
    if element<10:
        print(f"|   {element}", end="")
    if element>9 and element<100:
        print(f"|  {element}", end="")
    if element>100:
        print(f"| {element}", end="")
print("|")
print("-", end="")
print("-----"*8)