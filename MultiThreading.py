#Example 1
'''import threading
def display():
    print("Hello from thread")
t1 = threading.Thread(target= display)
t1.start()'''

#Example with two threads

'''import threading

def task1():
    for i in range(5):
        print("Task 1:", i)
def task2():
    for i in range(5):
        print("Task 2:", i)
t1 = threading.Thread(target= task1)
t2 = threading.Thread(target = task2)

t1.start()
t2.start()'''


#Join method
'''import threading

def task():
    for i in range(5):
        print(i)
t1 = threading.Thread(target = task)
t1.start()
t1.join()
print("Program completed")'''

#Passing arguements to a thread
'''import threading
def display(name):
    print("Hello", name)
t1 = threading.Thread(target = display, args = ("Keshika",))
t1.start()
t1.join()'''

#Example using multiple arguements
'''import threading
def addition(a, b):
    print("Sum =", a + b)
t1 = threading.Thread(target = addition, args= (10,20))
t1.start()
t1.join()'''

#Creating Multiple Threads
'''import threading
def print_numbers():
    for i in range(5):
        print("Numbers:", i)
def print_letters():
    for letter in "ABCDE":
        print("Letters:",letter)
t1 = threading.Thread(target = print_numbers)
t2 =  threading.Thread(target = print_letters)
t1.start()
t2.start()

t1.join()
t2.join()

print("All tasks completed")'''

#current thread

'''import threading
def task():
    print("Thread:", threading.current_thread().name)
t1 = threading.Thread(target=task)
t1.start()
t1.join()'''

#Naming a thread
'''import threading
def task():
    print("Running:", threading.current_thread().name)
t1 = threading.Thread(target=task, name="DownloadThread")

t1.start()
t1.join()'''

#Lock
'''import threading

lock = threading.Lock()

def task():
    lock.acquire()
    print("Critical section")
    lock.release()

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()'''


#import threading

#lock = threading.Lock()

'''def task():
    with lock:
        print("Critical section")

t1 = threading.Thread(target=task)
t2 = threading.Thread(target=task)

t1.start()
t2.start()

t1.join()
t2.join()'''

#Daemon thread

import threading
import time

def background_task():
    while True:
        print("Background running")
        #time.sleep(1)
t = threading.Thread(target=background_task)
t.daemon = True
t.start()
time.sleep(3)
print("Main program finished")



#ASSIGNMENT
#problem 1: Task scheduler simulation
import threading

def print_numbers():
    for i in range(1,6):
        print("Numbers:", i)

def print_letters():
    for letter in "ABCDE":
        print("Letters:", letter)

def print_square():
    for i in range(1,6):
        print(i ** 2)

t1 = threading.Thread(target=print_numbers)
t2 = threading.Thread(target=print_letters)
t3 = threading.Thread(target=print_square)

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()
print("All tasks completed!")


#Problem 2" File downloader simulation
'''import threading
import time
def download_file():
    print("Downloading{file_name}")
def background_task():
    while True:
        print("Background running")
        time.sleep(2)
t = threading.Thread()
t = threading.Thread(target = download_file )
t.daemon = True
t.start()
print("All downloads completed!")'''







    