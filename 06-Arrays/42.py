import random

def rand_elem(array):
    dlugosc = len(array)
    text = []
    for i in range(3):
        losowa = random.randint(0,dlugosc-1)
        text.append(array[losowa])
    
    text2 = "".join(str(text))
    return text2
        
array = [1,2,3,4,5,6,7,8,9]
print(rand_elem(array))

