# define vehicle class here

#Characterists:
# n_passangers
# size_cargo

#methods :
# accelerate
# break


class Vehicle():
    pass

    def __init__(self,n_passengers,cargo_size):
        self.n_passengers = n_passengers
        self.cargo_size = cargo_size

    def accelerate (self):
        return 'vroom'


    def breaking(self):
        return 'skrrrrr'
