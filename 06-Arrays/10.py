arr = [1,2,3,4,5]

print(arr)
#a
arr[0]-=1
print(arr)
#b
arr[-1]+=4
print(arr)
#c
arr[len(arr)//2] = arr[len(arr)//2] * 2
print(arr)