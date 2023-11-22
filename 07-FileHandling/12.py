def personal_data():
    name = str(input("Imie i Nazwisko: "))
    university = str(input("Uniwersytet: "))
    field = str(input("Kierunek: "))

    file = open("student.txt", "w")
    file.write(name+"\n")
    file.write(university+"\n")
    file.write(field+"\n")
    file.close()


personal_data()

