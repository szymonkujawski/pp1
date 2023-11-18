def f(product_code):
    string = product_code

    list = []

    for digit in string:
        list.append(digit)

    suma = 0
    for i in range(0,3):
        suma += int(list[i])

    reszta = suma%7

    if reszta==int(list[3]):
        return True
    else:
        return False
    
print(f("1082"))
print(f("2035"))
print(f("1114"))
print(f("7071"))