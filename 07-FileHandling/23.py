file = open("numbers3.txt", "w")

for i in range(1,11):
    if i<10:
        file.write(f"{i},{i**2},{i**3} {"\n"}")
    else:
        file.write(f"{i},{i**2},{i**3}")
