euro_buy_price = float(input("Bank buys EUR for: "))
euro_sell_price = float(input("Bank sells EUR for: "))

spread = euro_sell_price-euro_buy_price

spread = round(spread,4)

print(f"Spread: {spread:.4f}")