#Syntax
#new_list = [expression for item in iterable if condition]

#Example:
'''lst = [1,2,3,4,5,6,7,8,9,10]
#simple list comprehension
a = [x for x in lst]
print(a)'''

#Using IF with multiple if
#with multiple if
'''lst = [1,2,3,4,5,6,7,8,9,10]
d = [x for x in lst if x > 2 if x%2 == 0]
print(d)'''

#using if else with List Comprehension

'''lst = [1,2,3,4,5,6,7,8,9,10]
a = ['even' if x % 2 == 0 else 'odd' for x in lst]
print(a)'''

#using elif with list comprehension
'''a = [1,2,3,4,5,6,7,8,9,10]
b = ['even' if x % 2 == 0 else 'odd' for x in a]
print(b)'''

#List comprehension with a nested for loop
'''lst = [1,2,3]
lst_rev = [3,2,1]
g = [(x,y) for x in lst for y in lst_rev]
print(g)'''

#with functions
names = ["alice", "bob","charlie"]
capitalized = [name.capitalize() for name in names]
print(capitalized)