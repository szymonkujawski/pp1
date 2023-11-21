arr1 = [4,36,12,28,9,44,5]
arr2 = [5,1,36]
list = []

for number in arr1:
    if number not in arr2:
        list.append(number)

print(list)
