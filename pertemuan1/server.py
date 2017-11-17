import socket              

s = socket.socket()
port = 12345                
s.bind(('10.6.178.88', port))            
s.listen(5)                 
c,addr= s.accept()
while True:    
    x=c.recv(1024)
    print x
    y=raw_input()
    c.send(y)
