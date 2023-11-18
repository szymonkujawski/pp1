def f(n):
    x = 0
    y = 1
    tab = []
    # tab.append(x)
    tab.append(y)
    # for i in range(n-2): w zalezonsci czy zaczynamy od 0 czy od 1
    for i in range(n-1):
        tab.append(x+y)
        if i%2==0:
            x = x+y
        else:
            y = y+x
    return tab[-1]
    
print(f(10))