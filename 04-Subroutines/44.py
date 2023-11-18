def f(password):
    list = []
    for letter in password:
        list.append(letter)

    ilosc_unikalnych = len(set(list))

    if ilosc_unikalnych>=6:
        return True
    else:
        return False
   

print(f("ax15"))
print(f("book123"))
print(f("A2water3"))
print(f("qwerty"))
print(f(""))