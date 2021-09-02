#--------------------Libraries-----------------------
import queue
import time
import keyboard
import socket
import threading
from threading import Condition, Thread, Lock
import random

fruits = ["banana","apple","mango"]
print(fruits.pop(0))
queueFruits = []
lock = Lock()
condition = Condition()

def addFruitsInQueue(): #producer 
    global queueFruits
    while True:
        condition.acquire()
        chosenFruit = random.choice(fruits)
        print(f"adding fruit {chosenFruit} in queue ")
        queueFruits.append(chosenFruit)
        print(f"queue fruits after producing {queueFruits}")
        condition.notify()
        condition.release()
        time.sleep(1)


def eatFruits(): #consumer 
    global queueFruits
    while True:
        condition.acquire()
        if len(queueFruits) < 1:
            condition.wait()
        eatenFruit = queueFruits.pop(0)
        print(f"eated fruit : {eatenFruit}")
        print(f"queue fruits after consuming {queueFruits}")
        condition.release()
        time.sleep(1)

t1 = threading.Thread(target=addFruitsInQueue)
t2 = threading.Thread(target=eatFruits)

t1.start()
t2.start()