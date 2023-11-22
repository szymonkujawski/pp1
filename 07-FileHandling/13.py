list = ["film pierwszy","film drugi","film trzeci","film czwarty","film piaty"]

file = open("movies.txt", "w")
for title in list:
    file.write(title+"\n")
file.close()