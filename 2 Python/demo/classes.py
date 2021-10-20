

class Point():
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def distance(self, other):
        x = other.x - self.x
        y = other.y - self.y
        return f'{x}/{y}'



# point1 = Point()
# point2 = Point(2, 5)

# point2.x = 5
# point2.y = 8

# distance = point1.distance(point2)
# print(distance)


class Flight():
    def __init__(self, flight_number='', capacity=5, arrival_city='', departure_city='', arrival_time='', departure_time='', delayed=False):
        self.flight_number = flight_number
        self.__capacity = capacity
        self.passengers = []
        self.arrival_city = arrival_city
        self.departure_city = departure_city
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.delayed = delayed

    def add_passenger(self, name):
        if self.has_space():
            self.passengers.append(name)
        else:
            return False

    def has_space(self):
        if len(self.passengers) < self.__capacity:
            return True
        else:
            return False

    def __str__(self):
        return f"""
        Arrival: {self.arrival_city} {self.arrival_time}
        Departure: {self.departure_city} {self.departure_time}
        Capacity: {self.__capacity}
        Remaining Seats: {self.__capacity - len(self.passengers)}
        """

    def trip_duration(self):
        return self.arrival_time - self.departure_time / 60


fn001 = Flight(flight_number=1, capacity=10, departure_city='JFK', arrival_city='LAX', departure_time=800, arrival_time=1200)
fn234 = Flight(flight_number=234, departure_city='LAX', arrival_city='SEA', departure_time=1300, arrival_time=1600)

# first_flight = fn001.trip_duration()
# second_flight = fn234.trip_duration()


# print(fn001)


# Pet class
from names import names
import random
class Pet():
    def __init__(self, species='', name='', sex='', age=0, fixed=False, microchip=False):
        self.species = species
        self.name = name
        self.sex = sex
        self.age = age
        self.fixed = fixed
        self.microchip = microchip
    
    def __str__(self):
        return f'{self.name} -- {self.age}yo {self.species}'

species = ['cat', 'dog', 'snake', 'goldfish', 'rock', 'llama', 'bird']
sexes = ['M', 'F']
pets = []

for name in names:
    # get random species
    spec = random.choice(species)
    sex = random.choice(sexes)
    age = random.randint(0, 30)
    fixed = bool(random.randint(0,1))
    microchip = bool(random.randint(0,1))
    # create pet
    pet = Pet(name=name, species=spec, sex=sex, age=age, fixed=fixed, microchip=microchip)
    # add pet to pets list
    pets.append(pet)

print('somethign here')
print(['something here'])


