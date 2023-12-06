class TV():
    def __init__(self):
        self.is_on = False
    def turn_on(self):
        self.is_on = True
    def turn_off(self):
        self.is_on = False
    def show_status(self):
        if self.is_on:
            print("TV is on") 
        else:
            print("TV is off") 

set1 = TV()

set1.show_status()
set1.turn_on()
set1.show_status()