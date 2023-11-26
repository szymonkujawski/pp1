arr = [[-38, 19], [5,40],[-7,11],[29,16]]

smallest_elements = []
biggest_elements = []

for i in range(len(arr)):
    smallest_elements.append(min(arr[i]))

smallest_elements_x = smallest_elements.index(min(smallest_elements))
smallest_elements_y = arr[smallest_elements_x].index(min(smallest_elements))

for i in range(len(arr)):
    biggest_elements.append(max(arr[i]))

biggest_elements_x = biggest_elements.index(max(biggest_elements))
biggest_elements_y = arr[biggest_elements_x].index(max(biggest_elements))



print(f"Najmniejsza liczba to: {min(smallest_elements)} i znajduje się w {smallest_elements_x}, {smallest_elements_y}")
print(f"Największa liczba to: {max(smallest_elements)} i znajduje się w {biggest_elements_x}, {biggest_elements_y}")



