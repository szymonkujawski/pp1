def f(name):
    string = name

    list = string.split(" ")

    ilosc_elementow = len(list)
    
    list2 = []

    for i in range(0,ilosc_elementow):
        list2.append(list[i][0])
            
    return ''.join(list2)



print(f("To jest test"))