arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for row in arr:
    for element in row:
        print(element, end=" ")
    print()

arr_add = []
for i in range(len(arr)):
    arr_add.append(arr[i][0])

for i in range(len(arr)):
    arr[i][0] = arr[i][-1]

for i in range(len(arr)):
    arr[i][-1] = arr_add[i]


print("")

for row in arr:
    for element in row:
        print(element, end=" ")
    print()

