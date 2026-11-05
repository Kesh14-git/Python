#Example 1
'''def greet():
    print("Hello,welcome to Python!")
greet()'''

#Example 2 Function with parameters
'''def calculate_area(length,width):
    area = length * width
    return area
result = calculate_area(8,5)
print("Area of rectangle:",result)'''

#Example 3 Function with default parameters
'''def greet(name = "Guest"):
    print(f"Hello,{name}!")
greet("Alice")
greet()'''

#example 4 Function with return values
'''def square(number):
    return number ** 2
result = square(9)
print("Square of 9 is:",result)'''

#Example 5 Function with multiple return values

def sum_and_product(x,y):
    return x + y, x * y
result_sum,result_product = sum_and_product(3,4)
print("Sum:",result_sum)
print("Product:",result_product)



  
