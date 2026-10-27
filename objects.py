# Introduction to Object-Oriented Programming in Python
class Person:
    def __init__(self, name : str, gender : str, birth_year : int,
    email : str, phone : int):
        self.name = name
        self.gender = gender
        self.birth_year = birth_year
        self.email = email
        self.phone = phone
    
    def get_age(self, current_year : int) -> int:
        return current_year - self.birth_year

    def update_email(self, new_email : str) -> None:
        if "@" in new_email: # changes the current email to a new one
            self.email = new_email 
        else:
            raise ValueError("Invalid email!") # raises exception if incorrectly formatted (@ absent)


class Question: # The component class
    def __init__(self, question_instruction : str):
        self.question_instruction = question_instruction

    def get_question(self):
        print(self.question_instruction)

class Quiz: # The composite class
    def __init__(self, question_instruction : str):
        self.q = Question(question_instruction)

class Student(Person):
    def __init__(self, name: str, gender: str, birth_year: int, 
                 email: str, phone: int):
        super().__init__(name, gender, birth_year, email, phone)

class Subject:          # The component class
    def __init__(self, id, name, score):
        self.id = id
        self.name = name
        self.score = score
        

class Study_area:       # The composite class
    def __init__(self, id : str, name : str, score : int):
        self.subject = Subject(id, name, score)

class Major():
    def __init__(self, id : str, name : str, score : int):
        self.study_area = Study_area(id, name, score)

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
    def __init__(self, type: str, level: str, price: float):
        self.__type = type
        self.level = level
        self.price = price

    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, value):
        raise AttributeError("Insurance 'type' property is read-only")

    @type.deleter
    def type(self):
        raise AttributeError("Cannot delete insurance type")

# Instantiating the Insurance class
ins1 = Insurance('Dental', 'Ultimate', 299.99)

print(ins1.type)        # "Dental" — getter works
ins1.type = 'Life'      # Raises an AttributeError — setter blocks
del ins1.type           # Raises an AttributeError — deleter blocks

p1 = Person('Bruce Wayne', 'M', 1972, 'bruce.wayne@example.com', 404404404)

print(p1.get_age(2026)) # Age 54
p1.update_email('bruce.wayne@gotham.com') # Setter Works
print(p1.email)
p1.update_email('brucewaynegotham') # Raises a ValueError - does not pass setter validation
