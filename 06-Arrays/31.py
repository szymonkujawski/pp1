list = [2,3,2,5,8,1,9,8]

add_list = []

for number in list:
    if list.count(number)==1:
        add_list.append(number)

print("Array: ",end="")
for n in list:
    print(n, end=" ")

print()

print("Unique elements: ",end="")
for m in add_list:
    print(m, end=" ")