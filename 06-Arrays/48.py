def create_2d_arr(x,y):
    arr = [[0 for i in range(x)] for j in range(y)]
    for row in arr:
        for element in row:
            print(element, end=" ")
        print()
        
print(create_2d_arr(3,5))