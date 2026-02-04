from socket import*
s=socket()
s.bind(('127.0.0.1',45625))
s.listen(2)
print('Soket is listening')

while True:
    c,a=s.accept()
    print('Got connection from',a)
    sm=input('Message to client:')
    c.send(sm.encode())
    cm=c.recv(1024)
    print('message from client',cm.decode())
   
