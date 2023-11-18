dog_age_in_human_years = int(input("Enter the dog's age in human years: "))

if dog_age_in_human_years <= 2:
    print(f"The dog's age in dogs years is {dog_age_in_human_years*(10.5)} years.")
else:
    dog_age_in_human_years = dog_age_in_human_years-2
    print(21+(dog_age_in_human_years*4))