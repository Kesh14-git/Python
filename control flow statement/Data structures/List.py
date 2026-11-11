#an empty list
'''list =[] 
# A list with multiple data types
list = [1, "hello",3.14, True] 
#Acccessing List elements
list =[10,20,30,40]
print(list[0])
print(list[3])
#negative indexing
print(list[-1])
print(list[-2])'''

list =[] 
list =[10,20,30,40,"hello", 10,40,50] 
#method 1 :delete 
'''del list[3]
print(list)'''

#method 2:remove
'''print(list.remove("hello"))
print(list)'''

#method 3: pop
#print(list.pop(1))

#method 4:clear
#list.clear()
#print(list)
#print(list.count(10))

# Assignment - List
#1
'''list = ["apple","banana","strawberry","mango"]
print(list)'''

#2
'''list = [1,2,3,4,5,6,7,8,9,10]
print(list)'''

#Accessing elements
#Print first and last elements of a list
'''list = [10,20,30,40,50]
print(list[0])
print(list[-1])'''

#Access elements at index 3 in a list
'''list = [1,2,3,5,3,7,3]
print(list.index(3))'''

#Modify elements
#change value of an element at a specific index
'''list = [10,20,30,40,50]
print(list.index(2)= 100)'''

#replace a range of elements with a new list
'''a = [1,2,3,4,5]
b = [10,15,20,25]
a = temp
temp = b
b = a
print(a)'''

#Add elements
'''list = [10,20,30,40]
list.append(50)
print(list)'''

#Insert an element at specific index
'''list =[1,2,3,4,5]
list.index(2)
print(list[2])'''

#remove elements
'''list =[10,20,30,40,"hello"]
print(list.pop(4))'''

#remove element using remove()
'''list = [1,2,3,4,5]
list.remove(3)
print(list)'''

#List slicing
#create new list containing subsets from existing list
'''list = [1, 2,"appple",3,4]
sub_list = list[2:4]
print(sub_list)'''

#reverse list using slicing
list =[1,2,3,4,5]
a = list[::-1]
print(a)
 
