list = [7,3,8,5,2]
list_additional = [7,3,8,5,2]

def second_largest_number(list):
    list.sort()
    return list[-2]

def median(list):
    list.sort()
    if len(list)%2!=0:
        mid = len(list)//2
        return list[mid]
    else:
        sum_of_mid = list[len(list)//2]+list[(len(list)//2)-1]
        return sum_of_mid//2
    
def smallest_and_largest(list):
    maks = max(list)
    mini = min(list)

    return f"{mini},{maks}"
        
def numbers_as_string(list_additional):
    list1 = []
    for element in list_additional:
        list1.append(str(element))
    return "-".join(list1)

print(second_largest_number(list))
print(median(list))
print(smallest_and_largest(list))
print(numbers_as_string(list_additional))