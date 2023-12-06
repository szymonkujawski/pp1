class Phone():
    def __init__(self,brand,model,os_version):
        self.brand = brand
        self.model = model
        self.os_version = os_version
        self.is_turned_on = False
    def turn_on(self):
        self.is_turned_on = True
    def turn_off(self):
        self.is_turned_on = False
    def update_os_version(self, versionUpdate):
        self.os_version = versionUpdate

phone1 = Phone("Apple","IPhone 11",17.1)

print(f"Phone brand: {phone1.brand}")
print(f"Phone model: {phone1.model}")
print(f"Operating System Version: {phone1.os_version}")
# print(f"Is phone turned on: {phone1.is_turned_on}")
if phone1.is_turned_on:
    print(f"Currently turned on")
else:
    print(f"Currently turned off")


print(" ")

phone1.turn_on()
phone1.update_os_version(17.2)


print(f"Phone brand: {phone1.brand}")
print(f"Phone model: {phone1.model}")
print(f"Operating System Version: {phone1.os_version}")
# print(f"Is phone turned on: {phone1.is_turned_on}")
if phone1.is_turned_on:
    print(f"Currently turned on")
else:
    print(f"Currently turned off")
