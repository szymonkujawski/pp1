x = 0
y = 1
print(x)
print(y)
for i in range(18):
    print(x+y)
    if i%2==0:
        x = x+y
    else:
        y = y+x