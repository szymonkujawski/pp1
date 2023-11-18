washing_product = "shoes"
rinse = True
spin = False
washing_time = 0

if washing_product=="shoes":
    washing_time = washing_time + 20
elif washing_product=="jacket":
    washing_time = washing_time + 40
elif washing_product=="underwear":
    washing_time = washing_time + 70
else:
    washing_time = washing_time

if rinse==True:
    washing_time = washing_time + 15
else:
    washing_time = washing_time

if spin==True:
    washing_time = washing_time+9
else:
    washing_time = washing_time

print(f"Washing product: {washing_product}")
print(f"Rinse: {rinse}")
print(f"Spin: {spin}")
print(f"Total washing time: {washing_time} minutes")