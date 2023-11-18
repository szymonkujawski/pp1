height_cm = 170

height_inches = height_cm*0.393700787

height_feet = int(height_inches/12)

remainding_inches = round(height_inches%12)

print(f"I am {height_cm} cm tall, so im {height_feet} and {remainding_inches} inches tall.")