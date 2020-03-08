from vehicle_class import *


class Car(Vehicle):
    pass

    def __init__(self,n_passengers,cargo_size,brand,horsepower,max_speed):
        super().__init__ (n_passengers,cargo_size)
        self.brand = brand
        self.horsepower = horsepower
        self.max_speed = max_speed


    def park(self):
        return ' parking parking parking '

    def honk(self):
        return ' beep beep '




