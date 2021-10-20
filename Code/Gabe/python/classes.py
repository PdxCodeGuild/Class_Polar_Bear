import random
# message = str('Hello')
# number = int(4)

# print(type(message))
# print(type(number))

# print(message)
# print(number)

##### Creating a class #####

# class Point():
#   def __init__(self, x=0, y=0):
#     self.x = x
#     self.y = y

#   def distance(self, other):
#     x = other.x - self.x
#     y = other.y - self.y
#     return f'{x}/{y}'


# point1 = Point()
# point2 = Point(2, 5)

# point2.x = 5
# point2.y = 8

# distance = point1.distance(point2)

# # print(point1.x)
# # print(point1.y)
# # print(point2.x)
# # print(point2.y)
# print(distance)


###### Create another class ######

class Flight():
  def __init__(self, flight_number=0, capacity = 5, arrival_city = '', departure_city='', arrival_time='', departure_time='', delayed=False):
    self.flight_number = flight_number
    self.capacity = capacity
    self.passengers = []
    self.arrival_city = arrival_city
    self.departure_city = departure_city
    self.arrival_time = arrival_time
    self.departure_time = departure_time
    self.delayed = delayed

  def add_passenger(self, name):
    if self.has_space():
      self.passengers.append(name)
    else:
      return False

  def has_space(self):
    if len(self.passengers) < self.capacity:
      return True
    else:
      return False

  def __str__(self) -> str:
    return f"""
    Arrival: {self.arrival_city} {self.arrival_time}
    Departure: {self.departure_city} {self.departure_time}
    Capacity: {self.capacity}
    Remaining Seats: {self.capacity - len(self.passengers)}
    Occupancy: {len(self.passengers)}
    """


flight1 = Flight()

flight1.add_passenger('Steve')
flight1.add_passenger('Bob')
flight1.add_passenger('Andrew')
flight1.add_passenger('Susan')

# print(flight1.passengers)

dfw_pdx = Flight()

dfw_pdx.add_passenger('Reece')
dfw_pdx.add_passenger('James')
dfw_pdx.add_passenger('Mark')

# print(flight1)
# print(dfw_pdx)

fn001 = Flight(flight_number=1, capacity=10, departure_city='JFK', arrival_city='LAX', departure_time=2100, arrival_time=100)
fn234 = Flight(flight_number=234, departure_city='LAX', arrival_city='SEA', departure_time=200, arrival_time=500)

# print(fn001, fn234)


###### Another Class ######
from names import names # importing from names.py
class Pet():
  def __init__(self, species='', name='', sex='', age=0, fixed=False, microchip=False) -> None:
    self.species = species
    self.name = name
    self.sex = sex
    self.age = age
    self.fixed = fixed
    self.microchip = microchip

  def __str__(self) -> str:
    return f"{self.name} -- {self.age}yo {self.species}"

species = ['cat', 'dog', 'snake', 'fish', 'rock', 'llama', 'bird']
sexes = ['F', 'M']
pets = []

for name in names:
  # get random species
  spec = random.choice(species)
  sex = random.choice(sexes)
  age = random.randint(0, 30)
  fixed = bool(random.randint(0, 1))
  microchip = bool(random.randint(0, 1))
  # create pet
  pet = Pet(name=name, species=spec, sex=sex, age=age, fixed=fixed, microchip=microchip)
  # add to pets list
  pets.append(pet)
  print(pet)
