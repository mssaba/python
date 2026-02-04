from socket import *
s=socket()
try:
    s.connect(('127.0.0.1',45625))
    print('connected to server')
    print('Received',s.recv(1024).decode())
    sm=input('Message to server:')
    s.send(sm.encode())
except Exception as e:
    print('connection failed',e)
finally:
    s.close()
input('press enter to exit')