array = [4,2,6,3,5,7,23,12,4,9]

def greater(number):
    count = 0
    for element in array:
        if number<element:
            count +=1
    return count

print(greater(22))