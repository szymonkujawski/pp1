def f(n):
    text = "0"
    for i in range(1,n+1):
        z = str(i)
        text = text+z
    text = text[1:]
    return text

result = f(4)

print(result)
print(f(11))