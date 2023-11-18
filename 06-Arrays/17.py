list = [[0,0,0],[0,0,0],[0,0,0]]

for i in range(len(list)):
    list[i][i] = 1

for row in list:
    for element in row:
        print(element, end=" ")
    print()
