#Encapsulation in python using Public Members

'''class PublicExample:
    def __init__(self):
        self.public_attribute = 27

    def public_method(self):
        return "This is a public method."
obj = PublicExample()
print(obj.public_attribute)
print(obj.public_method())'''


#Encapsulation using Protected members

'''class ProtectedExample:
    def __init__(self):
        self._protectedattribute = 27

    def _protectedmethod(self):
        return "This is a protected method."
obj = ProtectedExample()
print(obj._protectedattribute)
print(obj._protectedmethod())'''


'''class Parent:
    def __init__(self):
        self._protected_var = 42

    def _protected_method(self):
        print("This is a protected method")

class Child(Parent):
    def access_protected(self):
        print(f"Accessing protected variable: {self._protected_var}")
        self._protected_method()

child_instance = Child()
child_instance.access_protected()
print(child_instance._protected_var)'''

#Encapsulation using Private members

'''class PrivateExample:
    def __init__(self):
        self.__private_attribute = 27

    def __private_method(self):
        return "This is a private method."

obj = PrivateExample()
print(obj.__private_attribute)
print(obj.__private_method())'''

'''class MyClass:
    def __init__(self):
        self.__private_attribute = 27
    def get_private_attribute(self):
        return self.__private_attribute
    def set_private_attribute(self,value):
        self.__private_attribute = value

my_instance = MyClass()
current_value = my_instance.get_private_attribute()
print("Current private attribute value:", current_value)

new_value = 100
my_instance.set_private_attribute(new_value)
print("Updated private attribute value:", my_instance.get_private_attribute())'''


'''class EncapsulationExample:
    def __init__(self):
        self.public_attribute = 42
        self._protected_attribute ="Protected"
        self.__private_attribute = [1,2,3]
    def public_method(self):
        print(self._protected_method())
        print(self.__private_method())
        print(self.__private_attribute)
        return "This is a public method"
        
    def _protected_method(self):
        
        return "This is a protected method"
       
    def __private_method(self):
        return "This is a private method"
    def get_private_attribute(self):
        return self.__private_attribute
    
E = EncapsulationExample()
print(E.public_method())
#print(E._protected_method())
#print(E._EncapsulationExample_private_method())'''

#


class BankAccount:
    def __init__(self,account_number,account_holder_name,balance):
        self.__account_number = account_number
        self.__account_holder_name = account_holder_name
        self.__balance = balance
    def get_account_holder_name(self):
        return self.__account_holder_name
    def set_account_holder_name(self,name):
        self.__account_holder_name = name
    def get_account_number(self):
        return self.__account_number
    def get_balance(self):
        return self.__balance
    def deposit(self,amount):
        if amount > 0:
            self.__balance += amount
            print("Deposit successful")
        else:
            print("Invalid deposit amount")
    def withdraw(self,amount):
        if amount <= 0:
            print("Invalid withdrawal amount")
        elif amount <= self.__balance:
            self.__balance -= amount
            print("Withdrawal successful")
        else:
            print("Insufficient balance")
obj = BankAccount(1234567890, "John Doe", 1000)

print(obj.get_account_number())
print(obj.get_account_holder_name()) 

obj.set_account_holder_name("John Smith")
print(obj.get_account_holder_name())

obj.deposit(500)
print(obj.get_balance())

obj.withdraw(700)
print(obj.get_balance())

