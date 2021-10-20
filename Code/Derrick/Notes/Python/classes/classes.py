# class Point():
#     def __init__(self,x=0,y=0):
#         self.x = x
#         self.y = y
#     def distance(self,o):
#         x = o.x - self.x
#         y = o.y - self.y
#         return f'{x}/{y}'


# point1 = Point(3,4)
# point2 = Point(5,9)

# distance = point1.distance(point2) 
# print(distance)

# class Flight():
#     def __init__(self,plane_num=000,capacity=100, arr='',dep='',arr_time=0,dep_time=0,delayed=False): # defines what to do first when class is called
#         plane_number = plane_num
#         self.capacity = capacity
#         self.passengers = []
#         self.arrival = arr
#         self.departure = dep
#         self.arrival_time = arr_time
#         self.departure_time = dep_time
#         self.delayed = delayed

#     def __str__(self):
#         return f'From {self.departure} to {self.arrival}\nCapacity: {self.capacity}\nRemaining seats: {self.capacity - len(self.passengers)}'

#     def add_passenger(self,first_name):
#         if len(self.passengers) >= self.capacity:
#             return False 
#         else:
#             self.passengers.append(first_name)

#     def has_space(self):
#         if len(self.passengers) < self.capacity:
#             return True
#         else:
#             return False

#     def flight_time(self,other):
#         total = ((other.arrival_time - other.departure_time) / 100) + ((self.arrival_time - self.departure_time) / 100)
#         return str(round(total, 0)) + ' hours'


# flight001 = Flight(dep='JFK',arr='LAX',dep_time=800,arr_time=1300)
# flight567 = Flight(plane_num=567,dep='LAX',arr='SEA',dep_time=1500,arr_time=1800)
# flight001.add_passenger('Bob')
# # flight1 = Flight()
# total = flight001.flight_time(flight567)

# print(total)

# flight1.add_passenger('Bob')
# flight1.add_passenger('Jim')
# flight1.add_passenger('Pam')
# flight1.add_passenger('Michael')

# dfw_pdx = Flight()
# dfw_pdx.add_passenger('Phyllis')
# dfw_pdx.add_passenger('Creed')
# dfw_pdx.add_passenger('Meredith')

# print(dfw_pdx)
import random 

class Pet():
    def __init__(self,animal='', name='', gender='', fixed=False, age=0):
        self.animal = animal
        self.name = name 
        self.gender = gender
        self.fixed = fixed
        self.age = age # months
    def __str__(self):
        return f'{self.name} is a {self.age} month old {self.animal}'

bob = Pet(animal='dog',name='Bob',gender='Male',fixed=True,age=2)

names = [
    'Tamia Gibson',
    'Arya Keith',
    'Tarun Plummer',
    'Boyd Morales',
    'Leen Beasley',
    'Terry Delarosa',
    'Mayson Sharma',
    'Liberty Cannon',
    'Kiara Cottrell',
    'Arif Couch',
    'Rodrigo Brennan',
    'Bea Timms',
    'Bertie Craig',
    'Izzie Guzman',
    'Chyna Bob',
    'Aaryan Serrano',
    'Emaan Conner',
    'Minahil Wilde',
    'Jonny Haney',
    'Edgar Mendez'
]
animals = ['cat','dog','spider','ferret','bird','hampster']
genders = ['Male','Female']
pets = []

for name in names:
    gender = random.choice(genders)
    animal = random.choice(animals)
    age = random.randint(0,(12*20))
    fixed = bool(random.randint(0,1))

    pet = Pet(name=name,gender=gender,animal=animal,age=age,fixed=fixed)
    pets.append(pet)

for pet in pets:
    print(pet)