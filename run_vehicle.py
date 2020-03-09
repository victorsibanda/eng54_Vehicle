# import all the classes

from vehicle_class import *
from car_class import *
from plane_class import *

# create 2 vehicle instances
vehicle1 = Vehicle(10,200)
vehicle2 = Vehicle(2,30)

# call methods and attributes to test
print('accelerate for vehicle 1 ', 'vehicle 2 cargo size', 'vehicle 1 breaking:')
print(vehicle1.accelerate())
print(vehicle2.cargo_size)
print(vehicle1.breaking(),'\n')


# create 2 car instances
car1 = Car(5,300,'Ford Mustang',410, '155 mph')
car2 = Car(2,300,'lamborghini aventador',566, '218 mph')
# make car accelerate and make them break
print('car 2 breaking and accelerating:')
print(car2.accelerate())
print(car2.breaking(),'\n')
# make car honk and park
print('car 1 honk and park:')
print(car1.honk())
print(car1.park(),'\n')

# create 2 plane instances here
plane1 = Plane(550,25200,'Boeing 777',110000, '1036 kmph')
plane2 = Plane(868,93000,'Airbus A380',180000, '1385 kmph')
# make plane accelerate and make them break
print('plane is accelerating and breaking:')
print(plane1.accelerate())
print(plane1.breaking(),'\n')
# make plane fly and land
print('plane is taking off and landing:')
print(plane2.take_off())
print(plane1.touchdown(),'\n')