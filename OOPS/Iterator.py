#Iterating through an iterator
#Example 1
'''my_list = [4,7,0]
iterator = iter(my_list)
print(next(iterator))
print(next(iterator))
print(next(iterator))'''

#for loop
'''my_list = [1,2,3,4,5]
iterator = iter(my_list)
for element in iterator:
    print(element)'''


#example3
'''class PowTwo:
    def __init__(self,max=0):
        self.max = max
    def __iter__(self):
        self.n = 0
        return self
    def __next__(self):
        if self.n <= self.max:
            result = 2 ** self.n
            self.n += 1
            return result
        else:
            raise StopIteration
numbers = PowTwo(3)
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))'''


#Assignment

class MultipleIterator:
    def __init__(self,x,n):
        self.x = x
        self.n = n
        self.count = 1
    def __iter__(self):
        return self
    def __next__(self):
        if self.x <= self.n:
            result = self.x * self.count
            self.count+= 1
            return result
        else:
            raise StopIteration
x = 5
n = 5
numbers = MultipleIterator(x,n)
i = iter(numbers)
print(next(i))
print(next(i))
print(next(i))
print(next(i))
print(next(i))
        


            