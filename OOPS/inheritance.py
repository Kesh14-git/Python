#Single Inheritance

'''class Animal(): #Parent/base class
    def sound(self):
        return "some sound"
class Dog(Animal): #child class/sub class
    def bark(self):
        return "woof"
d = Dog() #object
print(d.sound())
print(d.bark())'''


#Multilevel inheritance

'''class Animal:
    def speak(self):
        print("Animal Speaking")
class Dog(Animal):
    def bark(self):
        print("dog barking")
class DogChild(Dog):
    def eat(self):
        print("eating bread")
d = DogChild()
d.bark()
d.speak()
d.eat()'''

#Hierarchical inheritance

'''class Vehicle:
    def info(self):
        print("This is Vehicle")
class Car(Vehicle):
    def car_info(self,name):
        print("Car name is:",name)
class Truck(Vehicle):
    def truck_info(self,name):
        print("truck name is:",name)
obj1 = Car()
obj1.info()
obj1.car_info("BMw")
obj2 = Truck()
obj2.info()
obj2.truck_info("Ford")'''

#Multiple inheritance
'''class Calculation1:
    def Summation(self,a,b):
        return a + b
class Calculation2:
    def Multiplication(self,a,b):
        return a * b
class Derived(Calculation1,Calculation2):
    def Divide(self,a,b):
        return a / b;
d = Derived()
print(d.Summation(10,20))
print(d.Multiplication(10,20))
print(d.Divide(10,20))'''

#Hybrid inheritance
'''class Vehicle:
    def vehicle_info(self):
        print("Inside Vehicle class")

class Car(Vehicle):
    def car_info(self):
        print("Inside Truck class")

class Truck(Vehicle):
    def truck_info(self):
        print("Inside Truck class")

class SportsCar(Car,Vehicle):
    def sports_car_info(self):
        print("Inside SportsCar class")
s_car = SportsCar()
s_car.vehicle_info()
s_car.car_info()
s_car.sports_car_info()'''


#Inheritance assignment
#1
'''class Person:
    def greet(self,name,age):
        self.name = name 
        self.age = age 
        print(f"Hello,my name is {self.name},I am {self.age} years old.")
p = Person()
p.greet("arun",54)'''

#2
'''class Person:
    def show_name(self,age,name):
        self.name = name
        self.age = age
        print(f"My name is {self.name} and I am {self.age} years old.")
class Skills:
    def list_skills(self):
        print("The person has various skills.")
class Developer(Person,Skills):
    def programming_language:'''


#3
'''class Vehicle:
    def describe1(self):
        print("Vehicle")
class Car(Vehicle):
    def describe2(self):
        print("Car")
class Bike(Vehicle):
    def describe3(self):
        print("Bike")
c1 = Car()
c1.describe2()
c1.describe1()
c2 = Bike()
c2.describe3()
c2.describe1()'''



#4
'''class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
apple = Fruit("Apple","Red")
print(apple.name)
print(apple.color)'''

#5
'''class Teacher:
    def __init__(self,name,register_number):
        self.name = name
        self.register_number = register_number
    def display(self):
        print(f"Name is {self.name} and register number is {self.register_number}.")
t1.name("Alice")
t2.register_number(102)
t1.display()
t2.display()'''

'''class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def greet(self):
        print(f"Hello, my name is {self.name}")
p = Person("Keshika", 21)
p.greet()'''

'''class Person:
    def show_name(self,name,age):
        self.name = name
        self.age = age
        print(f"My name is {self.name}.")
class Skills:
    def list_skills(self):
        print(f"Has various skills.")
class Developer(Person,Skills):
    def __init__(self,language):
        self.programming_language = language
    def list_skills(self):
        print(f"Has various skills. Programming language: {self.programming_language}")
d = Developer("Python")
d.show_name("Alice",22)
d.list_skills()'''

'''class Vehicle:
    def __init__(self,type_of_vehicle):
        self.type_of_vehicle = type_of_vehicle
    def describe(self):
        print(f"The type of vehicle is {self.type_of_vehicle}.")
class Car(Vehicle):
    def __init__(self,type_of_vehicle,brand):
        super().__init__(type_of_vehicle)
        self.brand = brand
    def describe(self):
        print(f"The type of vehicle is {self.type_of_vehicle}.")
        print(f"The brand is {self.brand}")
class Bike(Vehicle):
    def __init__(self,type_of_vehicle,gear_count):
        super().__init__(type_of_vehicle)
        self.gear_count = gear_count
    def describe(self):
        print(f"The type of vehicle is {self.type_of_vehicle}.")
        print(f"The number of gears is {self.gear_count}")
c = Car("Car","BMW")
c.describe()

b = Bike("Bike",6)
b.describe()'''

class Fruit:
    def __init__(self,name,color):
        self.name = name
        self.color = color
    def display(self):
        print(self.name)
        print(self.color)
f = Fruit("Apple","Red")
f.display()


    
    

    
    




        