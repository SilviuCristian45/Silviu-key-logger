#--------------------Program purpose-------------------
#we wait 10 keys from the client 

#--------------------Libraries-------------------------
import socket
import keyboard

#--------------------Variables-------------------------
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 

#--------------------Algorithm-------------------------
s.bind( (socket.gethostname(), 1235) )                #create it on my machine 
s.listen(5)                                           #5 connections max 

clientsocket, address = s.accept()                #store the client socket + ipv4 address 
if not clientsocket:
    quit()

print(f"connection from {address}") 
while True:
    
    msg = clientsocket.recv(1024)                       #get what client sended to us
    print(msg.decode("utf-8"))               #print what the client sended to us 