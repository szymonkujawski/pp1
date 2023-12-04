orginal = open("countries.txt", "r")
copy = open("copy.txt", "w")

copy.write(orginal.read())

orginal.close()
copy.close()