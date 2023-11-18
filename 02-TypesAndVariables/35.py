tree_circumference  = float(input("Wprowadz obwod drzewa w cm: "))

tree_diameter = tree_circumference/3.141

tree_diameter = round(tree_diameter,3)

if tree_diameter>=50:
    print(f"Srednica drzewa wynosi: {tree_diameter} cm, wiec MOZE zostac sciete")
else:
    print(f"Srednica drzewa wynosi: {tree_diameter} cm, wiec NIE MOZE zostac sciete")
