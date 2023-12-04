import random

file = open("numbers2.txt", "w")

for i in range(50):
    if i<49:
        file.write(f"{random.randint(100,999)}{"\n"}")
    else:
        file.write(f"{random.randint(100,999)}")