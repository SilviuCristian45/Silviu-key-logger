#--------------------Program purpose-------------------
#we wait 10 keys from the client 

#--------------------Libraries-------------------------
import socket
import keyboard

#--------------------Variables-------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 

#--------------------Algorithm-------------------------
s.bind( (socket.gethostname(), 1234) )                #create it on my machine 
s.listen(5)                                           #5 connections max 

while True:
    clientsocket, address = s.accept()                #store the client socket + ipv4 address 
    print(f"Connection from {address} has been established !!!")
    msg = clientsocket.recv(1024)                       #get what client sended to us
    print(msg.decode("utf-8"),end="\n")               #print what the client sended to us 