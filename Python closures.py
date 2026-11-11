#Example 1
'''def greet(name):
    def display_name():
        print("Hi",name)
    display_name()
greet("John")'''

#Example 2
'''def greet():
    name = "John"
    return lambda: "Hi" + name
message = greet()
print(message())'''



#Example 3 : Print odd numbers using Python closures
'''def calculate():
    num = 1
    def inner_func():
        nonlocal num
        num += 2
        return num
    return inner_func
odd = calculate()
print(odd())
print(odd())
print (odd())

odd2 = calculate()
print(odd2())'''

#Example 4
'''def make_multiplier_of(n):
    def multiplier(x):
        return x * n
    return multiplier
times3 = make_multiplier_of(3)
times5 = make_multiplier_of(5)
print(times3(9))
print(times5(3))
print(times5(times3(2)))'''


#Assignment
#closure for a counter
 
def make_counter(step):
    count = 0
    def counter():
        nonlocal count

        count = count + step
        return count
    return counter
counter1 = make_counter(1)
counter5 = make_counter(5)

print(counter1())
print(counter1())
print(counter1())





    