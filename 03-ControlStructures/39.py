a = 7
b = 19

for i in range(1,a+1):
    if i==1 or i==a:
        print(b*"*")
    else:
        print(f"*{(b-2)*" "}*")