def f(x,y):
    list = []
    for i in range(x,y+1):
        if i%2==0 and i%3==0 and i%4!=0:
            list.append(i)

    suma = 0
    for element in list:
        suma += element

    return suma

print(f(1,20))
print(f(10,30))