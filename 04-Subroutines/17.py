a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
c = int(input("Enter third number: "))

def different(n1,n2,n3):
    if n1!=n2 and n1!=n3 and n2!=n3:
        return True
    else:
        return False
    
if different(a,b,c):
    print(f"Numbers {a} {b} {c} are different")
else:
    print("At least two numbers are the same")