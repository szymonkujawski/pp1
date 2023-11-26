text = "An apple a day keeps the doctor away"
text2 = text.split(" ")

def a(text2):
    return len(text2)

def b(text2):
    text3 = sorted(text2, key=len)
    return text3[::-1]

def c(text2):
    return sorted(text2)

print(a(text2))
print(b(text2))
print(c(text2))
