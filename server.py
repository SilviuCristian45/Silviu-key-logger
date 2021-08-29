#server script - we wait for the client (hacked) keywords 

import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #ipv4 tcp socket 

s.bind( (socket.gethostname(), 1234) )

s.listen(5) #maxim 5 conexiuni 

while True:
    clientsocket, address = s.accept() #stocam socketul clientului + adresa 
    print(f"Connection from {address} has been established !!!")
    #clientsocket.send() #we send information to the client 
    #get what client sended to us
    msg = clientsocket.recv(1024) #serverul primeste de la client man 
    print(msg.decode("utf-8"))