#Defining a class
'''class Student:
    def set_details(self,name,age):
        self.name = name 
        self.age = age
    def display(self):
        print(f"Student Name:{self.name},Age:{self.age}")
s1 = Student()
s1.set_details("Alice",20)

s2 = Student()
s2.set_details("Bob",22)

s1.display()
s2.display()'''


#Creating an Object and Class in python

'''class employee():
    def __init__(self,name,age,id,salary):
      self.name = name 
      self.age = age
      self.salary = salary
      self.id = id
emp1 = employee("harshit",22,1000,1234)
print(emp1.__dict__)

emp2 = employee("arjun",23,2000,2234)
print(emp2.name)
print(emp2.salary)'''


# Assignment Class and Objects

#1
'''class Car:
    def info(self,brand,model):
        self.brand = brand
        self.model = model
    def display(self):
        print(f"brand:{self.brand},Model: {self.model}")
c1 = Car()
c1.info("Tata","SUV")

c2 = Car()
c2.info("Ford","BMw")

c1.display()
c2.display()'''

#2 
'''class Student:
    def info(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Student name:{self.name},Age:{self.age}")
s1 = Student()
s1.info("Alice",20)
s2 = Student()
s2.info("Bob",19)
s3 = Student()
s3.info("Sam",20)

s1.display()
s2.display()
s3.display()'''

#3
'''class Rectangle:
    def info(self,length,width):
        self.length = length
        self.width = width
        print(self.length*self.width)

    
R1 = Rectangle()
R1.info(5,4)'''



#4 Bank account
'''class BankAccount:
    def info(self,account_number,balance):
        self.account_number = account_number
        self.balance = balance
    def deposit(self , deposite):
        self.balance += self.deposit
        print
    def withdraw(self,withdraw):
        self.balance -= self.withdraw
    def display(self):
        print(f"The amount deposited is{self.deposit} and withdraw amount is {self.withdraw}.")
b = BankAccount
b.info(678,56789)
b.deposit(788)
b.withdraw(100)
b.display()'''




#5 Circle Geometry
'''class Circle:
    def area(self,r):
        return pi* r ^ 2
    def circumference(self,r):
        return 2 * pi * r
a1 = Area()
a1.info()'''
    



#6 Employee Information
'''class Employee:
    def info(self,name,id,salary):
        self.name = name
        self.id = id
        self.salary = salary
    def bonus(self):
        print("The bonus of Employee is:")
    def display(self):
        print(f"My name is {self.name},my id is {self.id} and my salary is {self.salary}.")
e1 = Employee()
e1.info("Alice",102,5000)
e2 = Employee()
e2.info("Bob",103,4000)
e1.display()
e2.display()'''
    



#7 Library Management
'''class Book:
    def info(self,title,author,price):
        self.title = title
        self.author = author
        self.price = price
    def display(self):
        print(f"The book {self.title} wrtiten by {self.author} costs {self.price}. ")
b1 = Book()
b1.info("Diary of a young girl","Anne Frank",550)
b2 = Book()
b2.info("Harry Potter","J.K Rowling",350)
b1.display()
b2.display()'''

#8 Simple Calculator Class
'''class Calculator:
    def summation(a,b):
        return a + b
    def subtraction(a,b):
        return a - b
    def multiplication(a,b):
        return a * b
    def divide(a,b):
        return a / b
d = Calculator()
print(d.summation(2,3))
print(d.subtraction(5,4))
print(d.multiplication(4,5))
print(d.division(6,2))'''



#9 Student Marks System
'''class Student:
    def info(self,name,roll_no,marks):
        self.name = name 
        self.roll_no = roll_no
        self.marks = marks
    def calculate(self):
        total_marks = '''

#10 Inventory Management System
'''class Product:
    def info(self,product_id,name,price,quantity):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity'''

#11 Banking System with Multiple Accounts
'''class BankAccount:
    def info(self,deposit,withdraw,check_balance):
        self.deposit = deposit
        self.withdraw = withdraw
        self.check_balance = check_balance'''

#12 School Management
'''class Student:
    def info(self,name,id):
        self.name = name 
        self.id = id
class Teacher:
    def info(self,name,id):
        self.name = name
        self.id = id'''


'''class Student:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def display(self):
        print(f"Student name:{self.name}, Student age:{self.age}")
s1 = Student("Alice",22)
s1.display()'''


'''class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
    def display(self):
        print(f"Name : {self.name}, Salary : {self.salary}")
e1 = Employee("Ravi",25000)
e1.display()
e2 = Employee("Priya",30000)
e2.display()'''

#Rectangle Area
'''class Rectangle:
    def __init__(self,length,width):
        self.length = length
        self.width = width
    def area(self):
        area = self.length * self.width
        print(area)
r1 = Rectangle(10,5)
r1.area()'''

'''class BankAccount:
    def __init__(self,account_holdername,balance):
        self.account_holdername = account_holdername
        self.balance = balance
    def deposit(self,amount):
        self.balance = self.balance + amount
        print(self.balance)
    def withdraw(self,amount):
        self.balance = self.balance - amount
        print(self.withdraw)
account1 = BankAccount("Keshika", 5000)
account1.deposit(2000)
account1.withdraw(1000)'''

#Product
class Product:
    def __init__(self,product_name,price,quantity):
        self.product_name = product_name
        self.price = price
        self.quantity = quantity
    def total_price(self):
        total_price = self.price * self.quantity
        print(total_price)
p1 = Product("Laptop",5000, 2)
p1.total_price()









    


    









    

