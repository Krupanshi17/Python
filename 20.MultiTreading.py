"""MultiThreading 
When we run a python file,the os create something called process

Process=Running Program
Inside Process-Memory is allocated
               Cpu time is given 

inside  Process,code runs in a thread
Thread=excecution path

By default one thread exists and every python program starts with one thread 

example

print("A")
print("B")
print("C")

Execution:
    Main Thread:
    A -> B -> C 

This is single-threaded execution.

Problem Statement 
so we have a 2 task

1.download_file()  -> it takes 10 seconds
2.show_ui()

so show_ui() waits until the download_file() runs and program freez beacause main thread is busy in
downloading

this is where multithreading comes in 

Mutithreading means multiple threads inside the same process
Each thread does its own task and shares the same memory 


"""

#simplest Thread Example

import threading
def task():
    print("This task is running")

t=threading.Thread(target=task)
t.start()

import time

#adding time to understand the multithread process

def task():
    print("The task is running")
    time.sleep(3)
    print("The task end here")

t=threading.Thread(target=task)
t.start()

print("The print Statment Executes")


"""Join()
join() is a blocking call
Blocking means:
    Main thread stops
    waits patiently"""

def task():
    print("Task Started")
    time.sleep(3)
    print("Task Ended")

t=threading.Thread(target=task)
t.start()
t.join()

print("This is the main thread")

#Multiple Thread with join

def task1(name):
    print(name,"New Task Started")
    time.sleep(3)
    print(name,"New Task Ended")

t1=threading.Thread(target=task1,args=("Thread 1",))
t2=threading.Thread(target=task1,args=("Thread 2",))

t1.start()
t2.start()

t1.join()
t2.join()

print("This is the main thread")

#Race condition
"""Race Condition happens when the multiple threads can access and modify shared data
and the final outcome depends on the timing of execution"""

count=0
def increment():
    global count
    temp=count
    time.sleep(0.1)
    count=temp+1

threads=[]

for i in range(2):
    t=threading.Thread(target=increment)
    threads.append(t)
    t.start()


for t in threads:
    t.join()

print("Final Count",count)

"""We can fix this race condition problem using a lock
A way to allow only one thread at a time to access shared data.
A mechanism that prevents multiple threads from entering a critical section simultaneously."""

lock=threading.Lock()
count=0
def increament():
    global count
    with lock:
        temp=count
        time.sleep(0.1)
        count=temp+1

threads=[]

for i in range(2):
    t=threading.Thread(target=increament)
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("Final Count",count)


#A Ticket Booking Example
available_ticket=1
def book_ticket(name):
    global available_ticket
    with lock:

        if available_ticket>0:
            print("Found a seat")
            time.sleep(1)
            available_ticket-=1
            print(name, "booked the seat")
        else:
            print(name, "no seat available")

t1 = threading.Thread(target=book_ticket, args=("User A",))
t2 = threading.Thread(target=book_ticket, args=("User B",))

t1.start()
t2.start()

t1.join()
t2.join()

print("Seats left:", available_ticket)


