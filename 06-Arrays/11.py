def month(n):
    month_name = ["January", "February","March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
    return month_name[n-1]

n = int(input("Enter number: "))
print(month(n))
