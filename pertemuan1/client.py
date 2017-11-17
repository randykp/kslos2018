import socket              

s = socket.socket()         
host = socket.gethostname() 
port = 12345                
s.connect(('10.6.178.88', port))
while True:    
    x=raw_input()
    s.send(x)
    print s.recv(1024)  
