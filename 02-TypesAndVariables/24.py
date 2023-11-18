tablica_rejestracyjna = input("Enter vehicle registration number:: ")

if tablica_rejestracyjna[0]=="K" and (tablica_rejestracyjna[1]=="K" or tablica_rejestracyjna[1]=="R"):
    print(f"Car from Kraków: True")
else:
    print(f"Car from Kraków: False")