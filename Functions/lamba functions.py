#exapmle 1 Suimple lambda function
'''add_10 = lambda x : x + 10
print(add_10(5))'''

#Example 2 Lambda with Multiple arguements
'''multiply = lambda x,y: x * y
print(multiply(2,3))'''

#example 3 Using lambda with  map
# original list
'''numbers = [1,2,3,4]
squares = list(map(lambda x : x ** 2, numbers))
print(squares)'''


#Using lambda with filter
#Original list
'''numbers = [22,23,24,25,26]
even_numbers = list(filter(lambda x : x % 2 == 0,numbers))
print(even_numbers)'''

'''numbers = [61,62,63,64,65]
odd_numbers = list(filter(lambda x : x % 2 !=0,numbers))
print(odd_numbers)'''

#difference betweeen a lambda function and regular functiom
#lambda function
'''add = lambda x,y: x + y
print(add(3,5))'''

#regular function
'''def add(x,y):
    return x + y
print(add(3,5))'''




