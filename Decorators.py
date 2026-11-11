#Pass function as arguement
'''def add(x,y):
    return x + y
def calculate(func,x,y):
    return func(x,y)
result = calculate(add,4,6)
print(result)'''

#Return a function as a value
'''def greeting(name):
    def hello():
        return "Hello, " + name + "!"
    return hello
greet = greeting("Atlantis")
print(greet())'''

#Python Decorators(actual sum)

'''def make_pretty(func):
    def inner():
        print("I got decorated")
        func()
    return inner

def ordinary():
    print("I am ordinary")
decorated_func = make_pretty(ordinary)
decorated_func()'''




'''def star(func):
    def inner(*args, **kwargs):
        print("*" * 15)
        func(*args, **kwargs)
        print("*" * 15)
    return inner
def percent (func):
    def inner(*args, **kwargs):
        print("%" * 15)
        func(*args, **kwargs)
        print("%" * 15)
    return inner
@star
@percent
def printer(msg):
    print(msg)
printer("Hello")'''

'''def greet_all(*args):
    for name in args:
        print(f"Hello,{name}!")
greet_all("Alice","Bob","charlie")'''

'''def display_info(**kwargs):
    for key,value in kwargs.items():
        print(f"{key}:{value}")
display_info{name = "Alice", age = 30, city = "New York"}'''

def flexible_function(*args, **kwargs):
    print("Positional arguements:", args)
    print("Keyword arguements:", **kwargs)
flexible_function(1,2,3,name = "Alice", age = 30)




