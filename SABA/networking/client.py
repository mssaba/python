from socket import*
s=socket()
print('Connecting to server...')
s.connect(('127.0.0.1',45625))
print('Connected.Waitng for message...')
data=s.recv(1024)
print('Recieved:',data.decode())
s.close()
input('press enter to exit')