def compare(array1, array2):
    if len(array1)!=len(array2):
        return False

    i=0
    for element in array1:
        if element!=array2[i]:
            return False
        i+=1

        
    return True

print(compare(["water","book","sky"],["water","book","sky"]))
print(compare([True,False],[True,False,True]))
print(compare([5,3,1],[5,3,1]))
print(compare([3,2,1],[3,2]))