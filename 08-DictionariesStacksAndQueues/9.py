countries = [
    {"name":"Poland","population":38000000},
    {"name":"Germany","population":83200000},
    {"name":"Italy","population":59110000},
    {"name":"France","population":67750000},
    {"name":"Spain","population":47420000}
]

print(f"COUNTRY POPULATION")
# for key,value in countries.items():
#     print(f"{key} {value}")

for i in range(len(countries)):
    print(countries[i]["name"], end=" ")
    print(countries[i]["population"])