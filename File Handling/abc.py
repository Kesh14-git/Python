#Read mode
'''file = open("./File Handling/basic.txt", "r")

content = file.read()
print(content)

file.close()'''


#Write mode
'''file = open("./File Handling/basic.txt","w")
file.write("Welcome to Python")
file.close()'''

#append mode
'''file = open("./File Handling/basic.txt","a")
file.write("\n Python Programming")
file.close()'''

#Create mode
'''file = open("./File Handling/newfile.txt","x")
file.write = ("New File")
file.close()'''

#Reading file contents:
#read method()
'''file = open("./File Handling/basic.txt","r")
data = file.read()
print(data)
file.close()'''

#Example 2
'''file = open("./File Handling/basic.txt","r")
data = file.read(10)
print(data)
file.close()'''

#readline() method
'''file = open("./File Handling/basic.txt","r")
line = file.readline()
print(line)
file.close()'''

#readlines() method
'''file = open("./File Handling/basic.txt","r")
lines = file.readlines()
print(lines)
file.close()'''

#Writing data to a file
#write method()
'''file = open("./File Handling/basic.txt","w")
file.write("Artificial Intelligence")
file.write("\n Machine learning")
file.close()'''

#writelinesmethod()
'''file = open("./File handling/basic.txt","w")
lines = ["Deep learning\n","Natural Language Processing\n","Computer Vision\n"]
file.writelines(lines)
file.close()'''

#with open()

'''with open("./File Handling/basic.txt","r") as file:
    data = file.read()
    print(data)'''

#tell method()

'''with open("./File Handling/basic.txt","r") as file:
    print(file.read(8))
    print(file.tell())'''

#sek method()

'''with open("./File Handling/basic.txt","r") as file:
    print(file.read(5))
    file.seek(1)
    print(file.read(5))'''

#File modes with raed and write

'''with open("./File Handling/basic.txt","r+") as file:
    print(file.read())
    file.write("Hello")'''

'''with open("./File Handling/basic.txt","w+") as file:
    file.write("Python is a programming language")
    file.seek(0)
    print(file.read())'''

'''with open("./File Handling/basic.txt","a+") as file:
    file.write("\nJava")
    file.seek(2)
    print(file.read(5))'''

#Chyaracter encoding
with open("./File Handling/basic.txt","r",encoding="utf-8") as file:
    data = file.read()

with open("./File Handling/basic.txt","w",encoding="utf-8") as file:
    file.write(data)

#Examples
name = input("Enter Student name:")
age = input("Enter age:")
course = input("Enter course:")

with open("./File Handling/student.txt","w") as file:
    file.write("Student Details:\n")
    file.write("")
