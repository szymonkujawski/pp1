import json
movie = {
    "title":"Fight Club",
    "year":"1999",
    "actor":{"leading":"Edward Norton","supporting":"Brad Pitt"},
    "oscar":False,
    "earnings": 100000000
}

file = open("favourite.json", "w")

json.dump(movie, file, indent=6)
# ident to ilosc wciec na poczatku lini
file.close()