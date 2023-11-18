list = [[1,3,5],[8,7,2]]

# a
suma = list[0][0] + list[-1][-1]
print(suma)
# b
middle1 = len(list[0])//2
middle2 = len(list[1])//2
sumb = list[0][middle1]+list[1][middle2]
print(sumb)
# c
sumc = 0
for i in range(len(list[-1])):
    sumc += list[-1][i]

print(sumc)