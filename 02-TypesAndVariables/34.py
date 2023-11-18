vehicle_speed = int(input("Wprowadz predkosc pojazdu w km/h: "))

if vehicle_speed>=40 and vehicle_speed<=140:
    print(f"Predkosc {vehicle_speed} km/h JEST dozwolona na autostradzie")
else:
    print(f"Predkosc {vehicle_speed} km/h NIE JEST dozwolona na autostradzie")