file = open("countries2.txt", "r")

tab = []
for line in file:
    tab.append(line)

dlugosc = len(tab)
counter=1

status = ""
while status == "":
    if counter>=dlugosc+1:
        break

    print(f"{counter}. {tab[0]}")
    tab.pop(0)
    counter += 1

    if counter%6==0:
        status = input(str("Czekam na ENTER: "))

