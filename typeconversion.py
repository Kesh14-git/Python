#Implicit
'''x = 10
y = 10.5
z = x + y
print(type(z))'''

#Explicit

#1 String to integer
'''number ="100"
num = int(number)
print(type(num),num)'''

#2 Float to Integer
'''f = 1.7
i = int(f)
print(i,type(i))'''

#3 Integer to string
'''n = 10
string = str(n)
print(string,type(string))'''

#4 List to Tuple
'''MyList = [1,2,3,4]
MyTuple = tuple(MyList)
print(MyTuple,type(MyTuple))'''

#Practice programs
#Part A - Basic Programs

#prog1: Convert integer to float

'''num = int(input("Enter an integer:"))
result = float(num)

print("Original Integer:",num)
print("Converted Float:",result)'''

#program 2: Convert float to integer
'''num =float(input("Enter a float value:"))
result = int(num)
print("Original Float:",num)
print("Converted integer:", result)'''

#program 3:Convert integer to string
'''num = int(input("Enter an integer:"))
result= str(num)

print("Original Value:",num)
print("Converted String",result)
print("Data Type:",type(result))'''

#program 4:convert string to integer
'''num = input("Enter a number:")
result = int(num)

print("Converted Integer:",result)
print("Data Type:,type(result)")'''

#Convert character to ASCII value
'''ch = input("Enter a character:")
print("ASCII Value:",ord(ch))'''
 
 #Convert List to Tuple
'''numbers = [10,20,30,40]
result = tuple(numbers)
print("List:",numbers)
print("Tuple:",result)'''

#program 8: Convert Tuple to List
'''data = (5,10,15,20)
result = list(data)

print("Tuple:",data)
print("List:",result)'''

#9. Convert List to set
'''numbers = [10,20,30,40,10]
result = set(numbers)
print("Original List:",numbers)
print("Set:",result)'''

#10. convert set to list
'''data = {100,200,300,400}

result =list(data)
print("Set:",data)
print("List:",data)'''

#11. Convert String to list
'''word = input("Enter a word: ")
result =list(word)

print("List:",result)'''

#12 Convert List into string
'''letters = ['P','y','t','h','o','n']
result = "".join(letters)
print("String:",result)'''

#13 convert binary string to Decimal
'''binary = input("enter a binary number:")
decimal = int(binary,2)

print("Decimal Value:",decimal)'''

#14. convert decimal number to binary

'''num = int(input("Enter a decimal number:"))
binary = bin(num)
print("Binary:",binary)'''

#Convert Decimal Number to Ocatal and Hexadecimal
num = int(input("Enter a decimal number:"))
print("Octal:",oct(num))
print("Hexadecimal",hex(num))


 

