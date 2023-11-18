def f(number):
    one_count = 0
    two_count = 0
    three_count = 0
    four_count = 0
    five_count = 0
    six_count = 0
    seven_count = 0
    eight_count = 0
    nine_count = 0
    z = 0
    sum_of_all = 0

    while number > 0:
        z = number % 10
        if z==1:
            one_count += 1
        elif z==2:
            two_count += 1
        elif z==3:
            three_count += 1
        elif z==4:
            four_count += 1
        elif z==5:
            five_count += 1
        elif z==6:
            six_count += 1
        elif z==7:
            seven_count += 1
        elif z==8:
            eight_count += 1
        elif z==9:
            nine_count += 1
        number //= 10

    if one_count>=2:
        sum_of_all += one_count*1   
    if two_count>=2:
        sum_of_all += two_count*2
    if three_count>=2:
        sum_of_all += three_count*3   
    if four_count>=2:
        sum_of_all += four_count*4
    if five_count>=2:
        sum_of_all += five_count*5
    if six_count>=2:
        sum_of_all += six_count*6
    if seven_count>=2:
        sum_of_all += seven_count*7      
    if eight_count>=2:
        sum_of_all += eight_count*8
    if nine_count>=2:
        sum_of_all += nine_count*9

    return sum_of_all


print(f(1027))
print(f(230335))
print(f(513553007))