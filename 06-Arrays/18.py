list  = [[True,False],[True,True],[False,False]]

print(f"Before: {list}")

for i in range(len(list)):
    for j in range(len(list[i])):
        list[i][j] = not list[i][j]

print(f"After: {list}")