def f(expression):
    wynik = int(expression[0])

    for i in range(1,len(expression), 2):
        if expression[i]=="+":
            wynik += int(expression[i+1])
        else:
            wynik -= int(expression[i+1])

    return wynik


print(f("4+2+5-1"))