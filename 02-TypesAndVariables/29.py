import random

first_roll = random.randint(1,6)
second_roll = random.randint(1,6)
third_roll = random.randint(1,6)

sum_of_rolls = (first_roll+second_roll+third_roll)

print(f"Wyniki rzutow: {first_roll}, {second_roll}, {third_roll}, suma wynikow: {sum_of_rolls}")