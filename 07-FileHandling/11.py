file = open("11_text.txt", "r")

sum = 0
print("Numbers: ", end="")
for line in file:
    sum += int(line)
    print(int(line), end=" ")

print("")
print(f"Sum: {sum}")
