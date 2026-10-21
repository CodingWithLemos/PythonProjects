# Introduction to Object-Oriented Programming in Python
class Person:
    def __init__(self, name : str, gender : str, birth_year : int,
    email : str, phone : int):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.email = email
        self.phone = phone

class Question: 
    def __init__(self, question_instruction : str):
        self.question_instruction = question_instruction

    def get_question(self):
        print(self.question_instruction)

class Quiz:
    def __init__(self):
        self.q1 = Question('What is the meaning of Life?')
        self.q2 = Question('What do you do if Life gives you lemons?')
        self.q3 = Question('What is 2+2?')

class Student(Person):
    def __init__(self, name: str, gender: str, birth_year: int, 
                 email: str, phone: int):
        super().__init__(name, gender, birth_year, email, phone)

class Study_area:
    def __init__(self, id : str, name : str):
        self.name = name
        self.id = id

class Major(Study_area):
    def __init__(self, id : str, name : str):
        super().__init__(id, name)
        self.name = name

class Subject(Major):
    def __init__(self, id: str, name: str, score : int):
        super().__init__(id, name)
        self.id = id
        self.name = name
        self.score = score

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
    def __init__(self, name: str, gender : str, birth_year : int, email: str, 
                 phone: int, driver_id : str,
                 address : str):
        super().__init__(name, gender, birth_year, email, phone)
        self.driver_id = driver_id
        self.address = address

class Employee(Person): # Inherits from 'Person' parent class
    def __init__(self, name : str, gender : str, birth_year : int, email : str, 
                 phone : int, employee_id : int):
        super().__init__(name, gender, birth_year, email, phone)
        self.employee_id = employee_id

class Insurance:
    type = 'auto'

    def __init__(self, level : str, price : float):
        self.level = level
        self.price = price