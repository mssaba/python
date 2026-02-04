from socket import*
s=socket()
s.bind(('127.0.0.1',45625))
s.listen(1)
print('Socket is listening...')

c,addr= s.accept()
print('Got connection from',addr)
c.send(b'Thankyou for connecting')
c.close()
s.close()