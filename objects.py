# Introduction to Object-Oriented Programming in Python
class Person:
    def __init__(self, name : str, email : str, phone : int):
        self.name = name,
        self.email = email,
        self.phone = phone

class Car:
    def __init__(self, brand : str,
                 model : str,
                 license_plate : str, 
                 year : int, 
                 category : str, 
                 price_day : float,
                 status : str):
        self.brand = brand
        self.model = model
        self.license_plate = license_plate
        self.year = year
        self.category = category
        self.price_day = price_day
        self.status = status

class Customer(Person): # Inherits from 'Person' parent class
    def __init__(self, name: str, email: str, phone: int, driver_id : str,
                 address : str):
        super().__init__(name, email, phone)
        self.driver_id = driver_id
        self.address = address

class Employee(Person): # Inherits from 'Person' parent class
    def __init__(self, name : str, email : str, phone : int, employee_id : int):
        super().__init__(name, email, phone)
        self.employee_id = employee_id

class Insurance:
    type = 'auto'

    def __init__(self, level : str, price : float):
        self.level = level,
        self.price = price