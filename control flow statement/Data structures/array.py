#importing array module
'''import array as arr

#creating an array of integers
a = arr.array('i',[1,2,3,4,5])
print(a)'''

#Accesing  an array element
# import array as arr
'''a = arr.array('i',[1,2,3,4,5])
print(a[0])
print(a[4])'''

#array length
'''import array as arr
a = arr.array('i',[1,2,3,4,5])
length = len(a)
print(length)'''

#Modifying an array elements
#apppend
'''import array as arr
a = [1,2,3,45,6,78,100]
a.append(10)
print(a)'''

#pop()
'''import array as arr
a = [1,2,3,45,6,78,100]
a.pop(6)
print(a)'''

#remove()
'''import array as arr
a = [1,2,3,45,6,78,100]
a.remove(45)
print(a)'''

#Operations in array
#Concatenating - adding
'''import array as arr
b = arr.array('i',[2,3])
c = arr.array('i',[5,6])
d = arr.array('i')
d = b + c
print(d)'''

#Slicing
'''import array as arr
a = arr.array('i',[2,3,4,5,6])
#print(a[0:2])
print(a[::-1])'''

#Looping

'''import array as arr
a = arr.array('i',[2,3,4,5,6])
for x in a:
    print(x)'''

#while loop
'''import array as arr
a = arr.array('i',[2,3,4,5,6])
b = 0
while b < len(a):
    print(a[b])
    b = b+1'''

#Array value from user

from array import*
arr = array('i',[])
n = int(input("Enter the length of the array-5"))
for i in range(n):
    x = int(input("Enter the next value:"))
    arr.append(x)
    print(arr)


