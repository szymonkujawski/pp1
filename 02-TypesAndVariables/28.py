wzrost = int(input("Wprowadz wzrost w cm: "))
waga = int(input("Wprowadz wage w kg: "))

bmi = waga/((wzrost/100)**2)

print(f"Twoj wskaznik BMI wynosi: {bmi}")

if bmi>=18.5 and bmi<=25:
    print(f"BMI JEST w normie")
else:
    print(f"BMI NIE JEST w normie")