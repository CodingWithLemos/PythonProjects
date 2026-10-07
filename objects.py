# Introduction to Object-Oriented Programming in Python

class Car:
    def __init__(self, color : str, n_of_doors : int, engine : bool):
        self.color = color
        self.n_of_doors = n_of_doors
        self.engine = engine

    def describe(self):
        if self.engine:
            print('The color of the car is', self.color, 'it has', self.n_of_doors, 'doors, and has an engine.')
        else:
            print('The color of the car is', self.color, 'it has', self.n_of_doors, 'doors, and lacks an engine.')

class Customer:
    def __init__(self, 
                 name : str, 
                 gender : str, 
                 age = 18,
                 city = 'Lisbon', 
                 country = 'Portugal'):
        self.name = name,
        self.gender = gender,
        self.age = age,
        self.city = city,
        self.country = country

c1 = Car('red', 3, True)
c2 = Car('blue', 2, False)

cust1 = Customer('John Doe', 'Non-Binary', 25, 'Porto')
cust2 = Customer('Jane Doe', 'Female')

c1.describe()
c2.describe()

print(cust1.country)
print(cust2.name)
print(cust2.city)