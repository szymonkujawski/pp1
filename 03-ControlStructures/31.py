x = -1
y = 0

if x > 0:
    if y > 0 :
        print(f"Punkt P({x},{y}) jest w pierwszej cwiartce ukladu wspolrzednych")
    elif y < 0:
        print(f"Punkt P({x},{y}) jest w czwartej cwiartce ukladu wspolrzednych")
    else:
        print(f"Punkt P({x},{y}) znajduje sie na osi y")
elif x < 0:
    if y > 0:
        print(f"Punkt P({x},{y}) jest w drugiej cwiartce ukladu wspolrzednych")
    elif y < 0:
        print(f"Punkt P({x},{y}) jest w trzeciej cwiartce ukladu wspolrzednych")
    else:
        print(f"Punkt P({x},{y}) znajduje sie na osi y")
else:
    if y > 0:
        print(f"Punkt P({x},{y}) znajduje sie na osi x")
    elif y < 0:
        print(f"Punkt P({x},{y}) znajduje sie na osi x")
    else:
        print(f"Punkt P({x},{y}) znajduje sie na srodku ukladu wspolrzednych")