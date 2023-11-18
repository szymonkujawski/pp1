dlugosc_pierwszego_boku = int(input("Wprowadz dlugosc pierwszego boku: "))
dlugosc_drugiego_boku = int(input("Wprowadz dlugosc drugiego boku: "))
dlugosc_trzecia_boku = int(input("Wprowadz dlugosc trzeciego boku: "))

obwod = (dlugosc_pierwszego_boku+dlugosc_drugiego_boku+dlugosc_trzecia_boku)

polowa_obwodu = obwod/2

pole = (polowa_obwodu*(polowa_obwodu-dlugosc_pierwszego_boku)*(polowa_obwodu-dlugosc_drugiego_boku)*(polowa_obwodu-dlugosc_trzecia_boku))**(1/2)

print(f"Obwod tego trojkata wynosi: {obwod}, pole wynosi: {pole}")