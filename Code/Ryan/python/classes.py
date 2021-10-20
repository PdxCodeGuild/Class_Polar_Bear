# create a new class in python (this would be object in another language)

# custom classes created should be capitalized

# initializer function: what should be done when class is created

# always take at least one perameter (self)

from typing_extensions import TypeAlias


class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y
    def distance(self, other):
        x = other.x - self.x #anytime you reference the point you are in you identify it as self
        y = other.y - self.y
        return f'{x}/{y}'



point1 = Point(1, 1)
point2 = Point(2, 4)

# print(point1)

distance = point1.distance(point2)





class Flight():
    def __init__(self, capacity=5, arrival_city='', departure_city='', arrival_time='', departure_time='', delayed=False):
        # self.__capacity = capacity #makes it private variable that cannot be changed outside the method

        self.capacity = capacity
        self.passengers = []
        self.arrival_city = arrival_city
        self.departure_city = departure_city
        self.arrival_time = arrival_time
        self.departure_time = departure_time
        self.delayed = delayed
        
    def add_passenger(self, name): #this is considered a mehtod
        # if  len(self.passengers)  >= self.capacity:
        #     return False
        # else:
        #     self.passengers.append(name)
        if self.has_space():
            self.passengers.append(name)
        else:
            return False
    def has_space(self):
        if len(self.passengers) < self.capacity:
            return True
        else:
            return False
    def __str__(self): #the double underscore makes it a private method
        return f"""
        Arrival: {self.arrival_city} {self.arrival_time}
        Departure: {self.departure_city} {self.departure_time}
        Capcity: {self.capacity}
        Remaining Seats: {self.capacity - len(self.passengers)}
        """
    def trip_duration(self):
        return self.arrival_time - self.departure_time
# flight1 = Flight()

# flight1.add_passenger('steve')
# flight1.add_passenger('bob')
# flight1.add_passenger('susan')
# flight1.add_passenger('beth')


#flight1.passengers.append('Steve') #would allow you to add as many passengers as you would like which would allow you to create more passengers then capacity

#would be better to create a method


# dfw_pdx = Flight()
# dfw_pdx.add_passenger('Reece')
# dfw_pdx.add_passenger('James')
# dfw_pdx.add_passenger('Mark')


fn0001 = Flight(capacity=10, departure_city='JFK', arrival_city='LAX', departure_time=2100, arrival_time=100)

print(fn0001)

first_flight = fn0001.trip_duration()

# private method you can put a double _ and it can only be changed in the method

from names import names
import random
class Pet():
    def __init__(self, species='', name='', sex='', age='', fixed=False, microchip=False):
        self.species = species
        self.name = name
        self.sex = sex
        self.age = age
        self.fixed = fixed
        self.microchip = microchip
    def __str__(self):
        return f"""
        {self.name} --- {self.age}yo --- {self.species}"""

species = ['cat', 'dog', 'snake', 'goldfish', 'rock', 'llama', 'bird']
sexes = ['M', 'F']
pets = []

for name in names:
    #get random species
    spec = random.choice(species)
    sex = random.choice(sexes)
    age = random.randint(0, 30)
    fixed = bool(random.randint(0,1)) #random number 0 or 1 and convert into boolian (False or True)
    microchip = bool(random.randint(0,1))
    #create pet
    pet = Pet(name=name, species=spec, sex=sex, age=age, fixed=fixed, microchip=microchip)
    #add pet to list of pets
    pets.append(pet)