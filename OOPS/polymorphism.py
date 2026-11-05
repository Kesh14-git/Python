#Compile time Polymorphism(Method Overloading)
'''class Example:
    def show(self,a):
        print("One arguement:",a)
    def show(self,a,b):
        print("Two arguements:",a,b)
obj = Example()
obj.show(5,10) #works
obj.show(5) # Error'''

#Runtime Polymorphism(Method Overriding)
#Example1
'''class Animal:
    def sound(self):
        return"Some generic sound"
class Dog(Animal):
    def sound(self):
        return "Woof!"
class Cat(Animal):
    def sound(self):
        return "Meow!"
d = Dog()
print(d.sound())
c = Cat()
print(c.sound())'''

#Example 2:
'''class P:
    def properties_status(self):
        print("Money","Land","Gold")
    def to_marry(self):
        print("Anushka")
class C(P):
    def study_status(self):
        print("Studies done waiting for job")
    def to_marry(self):
        print("Megha")
c = C()
c. properties_status()
c.to_marry()
c.study_status()'''

#Example 1 : Using super in Method Overriding
'''class Animal:
    def speak(self):
        print("Animal speaks")
class Dog(Animal):
    def speak(self):
        print("Dog barks")
        super().speak()
dog = Dog()
dog.speak()'''

#Example @ :super in __init__ for initialization
'''class Person:
    def __init__(self,name):
        self.name = name
        print(f"Person named {self.name} is created")
class Employee(Person):
    def __init__(self,name,employee_id):
        super().__init__(name) #call the __init__ of person
        self.employee_id = employee_id
        print(f"Employee ID: {self.employee_id} is assigned")
emp = Employee("John","E123")'''


#POLYMORPHISM ASSIGNMENT
#1
'''class Shape:
    def area(self):
        print("Area calculation is not defined for this shape")
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
S = Shape()
C= Circle(2)
R = Rectangle(8,6)
T = Triangle(6,3)

print("Area of Circle:",C.area())
print("Area of Rectangle:",R.area())
print("Area of Triangle:",T.area())'''

#2
'''class Employee:
    def get_salary(self):
        return "Salary details not available"
        
class Manager(Employee):
    def __init__(self,name):
        self.name = name
        self.salary = 8000
    def get_salary(self):
        return self.salary
class Developer(Employee):
    def __init__(self,name,hourly_rate,hours_worked):
        self.name = name
        self.hourly_rate = hourly_rate
        self.hours_worked = hours_worked
    def get_salary(self):
        return self.hourly_rate * self.hours_worked
        
class Intern(Employee):
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary
        self.stipend = stipend
    def get_salary(self):
        return self.stipend
def print_salary(employee):
    print(employee.name,"Salary:",employee.get_salary())

manager1 = Manager("Bob")
developer1 = Developer("Charlie",50,160)
intern1 = Intern("David",30000)

print_salary(manager1)
print_salary(developer1)
print_salary(intern1)'''



#3 Library Mnagement system
'''class Book:
    def __init__(self,title,author,ISBN):
        self.title = title
        self.author = author
        self.ISBN = ISBN
    def display_info(self):
        print("Title",self.title)
        print("Author",self.author)
        print("ISBN",self.ISBN)
class EBook(Book):
    def __init__(self,title,author,ISBN,file_size):
            super().__init__(title,author,ISBN)
            self.file_size = file_size
    def display_info(self):
        super().display_info()
        print("File size",file_size, "MB")
class PrintedBook(Book):
    def __init__(self,title,author,ISBN,file_size,pages):
        super().__init__(title, author, ISBN)
        self.pages = pages

    def display_info(self):
        super().display_info()
        print("Pages:", self.pages)
B = Book("Python Basics","Bob","ISBN001")
E = EBook("AI","Charlie","ISBN002",5)
P = PrintedBook("Data Science","Alice","ISBN003",450)

print("Book Details:")
B.display_info()

print("\nEBook Details:")
E.display_info()

print("\nPrintedBook Details:")
P.display_info()'''


'''class Shape:
    def area(self):
        return "Area is not defined for this shape"
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
def print_area(shape):
        print(shape.area())


c = Circle(5)
r = Rectangle(6,8)
t = Triangle(3,15)

print_area(c)
print_area(r)
print_area(t)'''

class Employee:
    def get_salary(self):
        return "Salary details not available."
class Manager(Employee):
    def __init__(self,salary):
        self.salary = salary
    def get_salary(self):
        return self.salary
class Developer(Employee):
    def __init__(self,hourly_rate,hourly_worked):
        self.hourly_rate = hourly_rate
        self.hourly_worked = hourly_worked
    def get_salary(self):
        return self.hourly_rate * self.hourly_worked
class Intern(Employee):
    def __init__(self,stipend):
        self.stipend = stipend
    def get_salary(self):
        return self.stipend
def  print_salary(employee):
     print(employee.get_salary())

M = Manager(8000)
D= Developer(9,8)
I = Intern(15000)

print_salary(M)
print_salary(D)
print_salary(I)







        

