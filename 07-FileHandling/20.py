meatandfish = open("MeatAndFish.txt", "r")
grainsandbread = open("GrainsAndBread.txt", "r")
allproducts = open("allproducts.txt", "w")

for lines in meatandfish:
    allproducts.write(lines)

allproducts.write("\n")

for lines2 in grainsandbread:
    allproducts.write(lines2)

meatandfish.close()
grainsandbread.close()
allproducts.close()