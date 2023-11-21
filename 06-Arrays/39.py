def separate(list):
    list2 = []
    for element in list:
        if element%2==0:
            list2.append(element)
    
    for element in list:
        if element%2!=0:
            list2.append(element)

    return list2

list = [1,2,3,4,5,6,7,8,9]

print(separate(list))
