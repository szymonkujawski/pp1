first_name = str(input("Enter first name: "))
first_person_age = int(input("Enter first person age: "))

second_name = str(input("Enter second name: "))
second_person_age = int(input("Enter second person age: "))

if first_person_age >= 18 and second_person_age >= 18:
    print(f"Both {first_name} and {second_name} are adults")
else:
    print(f"One or both of them aren't adults")