file = open("numbers.txt", "w")

for i in range(1,51):
    if i<50:
        file.write(f"{i} {"\n"}")
# zeby nie przechodzilo do nastepnej lini na koncu
    else:
        file.write(f"{i}")

file.close()