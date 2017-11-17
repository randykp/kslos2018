import time

mySocket = socket.socket()
mySocket.connect((SERVER_IP,PORT_NUMBER))

while True:
        mySocket.send('cool')
        time.sleep(.5)
