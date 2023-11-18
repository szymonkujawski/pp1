def f(number, even):
    sum = 0
    if even==True:
        while number > 0:
            last = number % 10
            if last % 2 == 0:
                sum += number % 10
            number //= 10
    else:
        while number > 0:
            last = number %10
            if last%2!=0:
                sum += number % 10
            number //= 10
    return sum

print(f(3124,True))
print(f(3124,False))
print(f(20576,False))
print(f(20576,True))
print(f(13115,True))
