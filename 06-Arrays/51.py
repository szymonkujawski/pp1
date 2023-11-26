arr = [[1,2,3,4,5],[6,7,8,9,10],[11,12,13,14,15]]

for row in arr:
    for element in row:
        print(element, end=" ")
    print()

arr_add = []

arr_add = arr[0]
arr[0] = arr[-1]
arr[-1] = arr_add

print()

for row in arr:
    for element in row:
        print(element, end=" ")
    print()