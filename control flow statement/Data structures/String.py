#Common string methods

#Define a string
#text = "hello WoRLd"
#str = "python"

#convert to uppercase
#print(text.upper())

#convert to lowercase
#print(text.lower())

#capitalize
#print(text.capitalize())

#Title
#print(text.title())

#swapcase
#print(text.swapcase())
'''str = "Artificial Intelligence"
print(str.swapcase())'''

#Modification methods

#str.strip()
#text = "  Hello World  "
#print(text.strip())

#str.lstrip()
#print(text.lstrip())

#str.rstrip
#print(text.rstrip())

#str.replace(old,new)
'''text_replace = "Hello World,Welcome to the World of Python"
print("Replace World with Universe:",text_replace.replace("World","Universe"))'''

#Splitting and Joining

#str.split(delimiter)
#text = ("apple,banana,cherry")
#print(text.split(","))

#str.rsplit(delimiter)
#print(text.rsplit(",", 1))

#str.partition(delimiter)
#print(text.partition("banana"))

#str.join(iterable)
#print(",".join(text))

'''words = ("Python","is","awesome")
print(" ".join(words))'''

#Character checks
#str.isalpha()
'''alpha_str = "Python"
print(alpha_str.isalpha())'''

#str.isdigit()
#digit_str ="12345"
#print(digit_str.isdigit())

#str.isalnum()
'''alnum_str = "Python3"
print(alnum_str.isalnum())'''

#str.isspace()
'''space_str = " "
print(space_str.isspace())'''
'''mixed_str = "Python 3"
print(mixed_str.isspace())'''

#len(str)
text = "Python"
#print(len(text))

#Indexing
#print(text[4])

#Slicing
#print(text[2:3])

#Formatting
#str.format()
name = "Alice"
age = 25
#print("My name is {} and I am {} years old".format(name,age))'''

#str.zfill(width)
'''number = "42"
print(number.zfill(5))'''

#f strings
'''height = 5.8
print(f"My name is {name}, I am {age} years old and my height is {height} feet.")'''

'''num1, num2 = 10,20
print(f"Sum  of {num1} and {num2} is {num1 + num2}.")'''


#Practice questions
#1 Count characters
'''text = "Hello World"
print(len(text))
print(text.count)'''

#2 Reverse a string
'''text = "Python"
print(text[::-1])'''

#3 Count Vowels and consonants
text = "Artificial Intelligence"
vowel = ["a","e","i","o","u"]




#4 Check palindrome
#text = "madam"
'''text = "Python"
if text[::1] 
    print("palindrome")
else:
    print("Not a palindrome")'''





#5 Find character frequency
text = "banana"
print(text.count('b'))
print(text.count('a'))
print(text.count('n'))




      
