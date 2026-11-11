#Using a Generator function
'''def count_up_to(max_value):
    count = 1
    while count <= max_value:
        yield count
        count+= 1
generator = count_up_to(5)
for value in generator:
    print(value)'''

#Example 2
'''squares_generator =(i * i for i in range(5))
for i in squares_generator:
    print(i)'''

#Example 3
class PowTwo:
    def __init__(self,max=0):
        self.n = 0
        self.max = max
    def __iter__(self):
        return self
    def __next__(self):
        if self.n > self.max:
            raise StopIteration
        result = 2 ** self.n
        self.n += 1
        return result

#Example 4
'''def PowTwoGen(max = 5):
    n = 0
    while n < max:
        yield 2 ** n
        n += 1
    for n in PowTwoGen(5):
        print(n)'''

def fibonaccci_numbers(nums):
    x,y = 0,1
    for i in range(nums):
        x,y = y, x+y
        yield x
def square(nums):
    for num in nums:
        yield num ** 2
    print(sum(square(fibonnaci_numbers(10))))


#Assignment
 
def fibonacci_numbers(nums):
    x,y = 0,1
    for i in range(nums):
        x,y = y, x+y
        yield x
