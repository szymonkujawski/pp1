number_of_products = int(input("Enter number of products: "))
product_price = int(input("Enter product price: "))


print(f"Numbers of products purchased: {number_of_products}")
print(f"Product price: {product_price}")

if number_of_products<=2:
    print(f"Amount to pay: {number_of_products*product_price}")
else:
    print(f"Amount to pay: {(2*product_price)+(number_of_products-2)*0.75*product_price}")
