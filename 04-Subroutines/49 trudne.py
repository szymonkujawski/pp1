def f(dice):
    row = 1
    num = dice[0]
    tmp = 1
    for i in range(0,len(dice)-1):
        if dice[i] == dice[i+1]:
            tmp += 1
        if tmp > row:
            num = dice[i]
            row = tmp
            tmp = 1

    return num

print(f("5233165554211"))
print(f("2133"))