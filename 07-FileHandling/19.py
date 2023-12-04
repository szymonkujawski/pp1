orginal = open("countries.txt", "r")
copy = open("copylines.txt", "w")

for lines in orginal:
    copy.write(lines)

orginal.close()
copy.close()