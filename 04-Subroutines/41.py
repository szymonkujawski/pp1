def f(n):
    i = 0
    list = []
    while len(list)<n:
        i += 1
        dzielnik = 0
        for j in range(1,i+1):
            if i%j==0:
                dzielnik +=1
        if dzielnik==2:
            list.append(i)

    return list[-1]

print(f(9))


