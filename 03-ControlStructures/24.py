price = 200
price_after_discount = 170
discount = 1-(price_after_discount/price)

discount = round(discount,2)

percentage = discount*100
percentage = int(percentage)

print(f"Current product price {price_after_discount}")
print(f"Prevoius product price {price}")

if discount>=0.3:
    print(f"Buy this product!!!")
    print(f"Product price reduced by {percentage}%")
else:
    print(f"Product price reduced by {percentage}%")
