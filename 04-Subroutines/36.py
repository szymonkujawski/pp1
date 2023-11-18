def f(detector):
    count = 0
    three = False
    for i in range(0,len(detector)):
        sign = detector[i]
        if sign=="+":
            count += 1
        else:
            count -= 1
        if count==3:
            three = True
    return three

print(f("+-+++-+---"))
print(f("+-+-+-+-"))
print(f("+-++-+--"))
print(f("+-++-++-+---"))
