def f(n1,n2,operator):
    if operator=="+":
        return n1+n2
    elif operator=="-":
        return n1-n2
    elif operator=="*":
        return n1*n2
    elif operator=="/":
        return n1/n2
    elif operator=="%":
        return n1%n2
    elif operator=="**":
        return n1**n2       
    
print(f(2,3,"+"))    
print(f(2,3, "%"))    
print(f(2,3, "**"))    
print(f(2,3, "*"))    
print(f(2,3, "-"))    