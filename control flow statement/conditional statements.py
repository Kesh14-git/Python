'''age = int(input("Enter your age:"))
if age > 18:
    print("Eligible to vote")
else:
    print("Not Eligible to vote")'''

'''age = int(input("Enter your age:"))
if age < 10:
    print("You are a child")
elif age < 20:
    print("You are a teenager")
elif age < 50:
    print("You are an adult")
else:
    print("You are a senior citizen")'''

#Nested if
'''num = int(input("Enter a number:"))
if num > 0:
    print("The number is positive")
    if num % 2 == 0:
        print("Number is even")
    else:
        print("Number is odd")
elif num < 0:
    print("The number is negative")
else:
    print("The number is zero")'''

#Complex conditions

'''age = int(input("Enter your age:"))
if age >= 18:
    print("You are eligible to vote")
    if age >= 18:
        print("You are eligible to vote:")
        if age >= 65:
           print("You are also eligible for senior citizen benefits:")
    else:
        print("You are not eligible to vote:")'''

#Categorization
'''score = int(input("Enter your score :"))
if score >= 90:
    print("Grade A")
    if score == 100:
        print("Perfect Score!")
elif score >= 80:
    print("Grade B")
elif score >= 70:
    print("Grade C")
else:
    print("Grade D")'''

#Input Validation
'''username = input("Enter your username:")
if len(username) > 0:
    if username.isalnum():

        print("username is valid")
    else:
        print("username does not contain letters or numbers")
else:
    print("username is not valid")'''

#4 Decission trees
'''temperature = float(input("Enter the temperature in Celsius:"))
if temperature <0:
    print("It is freezing!")
    if temperature < -10:
        print("It is extremely cold!")
elif temperature < 20:
        print("Its cool")
else: 
    print("Its warm")'''

#Practice problems

#ATM Minimum Balance

'''balance = float(input("Enter Account Balance:"))
if balance < 1000:
   print("Minimum Balance Not Maintained")'''

#Online Shopping Discount
'''amount = float(input("Enter purchase amount:"))
if amount >= 5000:
    print("Discount Applied")
else:
    print("No Discount")'''

#Mobile Battery Alert

'''battery = int(input("Enter Battery Percentage:"))
if battery < 20:
   print("Low battery! Please Charge")
else:
   print("Battery level is good ")'''

#Speed limit Check
'''speed = int(input("Enter Speed:"))
if speed > 80:
    print("Speed Limit Exceeded")
else:
    print("Drive Safely")'''

#Employee Bonus
'''years = int(input("Enter Years of Service"))

if years >10:
    print("Bonus:10000")
  elif years >=5:
    print("Bonus:5000")
else:
    print("No Bonus")'''

#Fuel Warning System
'''fuel = int(input("Enter Fuel Percentage:"))

if fuel <10:
    print("Fuel Empty")
elif fuel <=25:
    print("Low Fuel")
elif fuel <= 75:
    print("Fuel OK")
else:
    print("Fuel Tank Full")'''

#Student Attendance
'''attendance = float(input("Enter Attendance Percentage:"))
if attendance >= 75:
    print("Eligible for exam")
elif attendance >=60:
    print("Eligible for exam")
else:
    print("Not Eligible for exam")'''

#College Admission
status = input("Have you passed Class 12(yes/no):")
percentage = float(input("Enter by your percentage:"))


if status == "yes":
    if percentage >= 75:
       print("Admission Approved")
    else:
        print("Admisssion Rejected due to Low Marks")
else:
    print("Not Eligible for admission")    



