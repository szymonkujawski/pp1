n = int(input("Enter number: "))
x = 0
i = 0
while x < n:
    i += 1
    dzielnik = 0
    for j in range(1,i+1):
        if i%j==0:
            dzielnik = dzielnik + 1
    if dzielnik==2:
        print(i)    
        x += 1

        