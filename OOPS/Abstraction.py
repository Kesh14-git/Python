'''from abc import ABC, abstractmethod
class Car(ABC):
    def mileage(self):
        pass
class Tesla(Car):
    def mileage(self):
        print("The mileage is 30kmph")
class Suzuki(Car):
    def mileage(self):
        print("The mileage is 25kmph")
class Duster(Car):
    def mileage(self):
        print("The mileage is 24kmph ")
class Renault(Car):
    def mileage(self):
        print("The mileage is 27kmph")
t = Tesla()
t.mileage()

r = Renault()
r.mileage()

s = Suzuki()
s.mileage()
d = Duster()
d.mileage()'''


'''from abc import ABC
class llgm(ABC):
@abstract method
    def calculate_area(self):
        pass
class Square(llgm):
    length = 5
    def calculate_area(self):
        return self.length * self.length
class Circle(llgm):
    radius = 4
    def calculate_arae(self):
        return 3.14 *self.radius *self.radius
sq = Square()
cir =Circle()
print("Area of square:",sq.Area())
print("Area of circle:",cir.Area())'''


#Abstraction assignment

#1
'''from abc import ABC
class Animal:
    @abstractmethod
    def make_sound(self):
        pass
class Dog(Animal):
    def make_sound(self):
        return "Woof!"
class Cat(Animal):
    def make_sound(self):
        return "Meow!"
class Cow(Animal):
    def make_sound(self):
        return "Moo!"
Dog = Dog()
Cat = Cat()
Cow = Cow()
print(Dog.make_sound())
print(Cat.make_sound())
print(Cow.make_sound())'''


#2
'''from abc import ABC, abstractmethod
class Shape(ABC):
    def area(self):
        pass
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
    def area(self):
        return 3.14 * self.radius ** 2
class Rectangle(Shape):
    def __init__(self,length,width):
         self.length = length
         self.width = width
    def area(self):
        return self.length * self.width
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    def area(self):
        return 0.5 * self.base * self.height
C = Circle(4)
R = Rectangle(5,3)
T = Triangle(6,2)'''


#3 Payment Gateway System

from abc import ABC, abstractmethod

class PaymentMethod(ABC):


class CreditCard(PaymentMethod):
    def __init__(self, card_number):
        self.card_number = card_number

    def validate_account(self):
        print("Credit Card account validated")

    def pay(self, amount):
        print("Paid", amount, "using Credit Card")

class PayPal(PaymentMethod):
    def __init__(self, email):
        self.email = email
    def validate_account(self):
        print("PayPal account validated")
    def pay(self, amount):
        print("Paid", amount, "using PayPal")
class BankTransfer(PaymentMethod):
    def __init__(self, account_number):
        self.account_number = account_number
    def validate_account(self):
        print("Bank account validated")
    def pay(self, amount):
        print("Paid", amount, "using Bank Transfer")

C = CreditCard("1234567890")
P = PayPal("user@gmail.com")
B = BankTransfer("9876543210")

C.validate_account()
C.pay(500)
P.validate_account()
P.pay(1000)
B.validate_account()
B.pay(1500)

#4 Vehicle Management System
from abc import ABC, abstractmethod
class Vehicle:
    def __init__(speed):
        self.speed = speed
class Car:
    def __init__(Vehicle):

#5 Abstract Remote  Control
class RemoteControl:
    def __init__():

class TVRemote(RemoteControl):



class MusicSystemRemote(RemoteMethod):






