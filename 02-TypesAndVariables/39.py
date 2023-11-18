price = float(input("Wprowadz cene: "))
discount = int(input("Wprowadz upust w %: "))
reduction = price*(discount/100)
price_with_discount = price-reduction
reduction = round(reduction,2)
price_with_discount = round(price_with_discount,2)

print(f"Price with discount: {price_with_discount}")
print(f"Reductiion: {reduction}")