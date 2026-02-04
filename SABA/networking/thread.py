# import threading,time
# def name(s):
#     print(f'Name: {s}')
#     time.sleep(2)
# t=threading.Thread(target=name,args=("SABAPATHY MS",))
# t.start()
# t.join()
# print('succesful')    

import threading, time

l=threading.Lock()
def task(name):
    for i in range(3):
        l.acquire()
        print(f"{name} running {i}")
        l.release()
        time.sleep(5)
t1=threading.Thread(target=task, args=("Thread 1",))
t2=threading.Thread(target=task, args=("Thread 2",))
t3=threading.Thread(target=task, args=("Thread 3",))
t1.start(); t2.start(); t3.start()
t1.join(); t2.join(); t3.join()

# import threading,time
# def sqr(num):
#     print(f'SQUARE:{num*num}')
#     time.sleep(2)
# def cub(num):
#     print(f'CUBE:{num*num*num}')

# a=threading.Thread(target=sqr,args=(4,))
# b=threading.Thread(target=cub,args=(2,))
# a.start();a.join()
# b.start();b.join()
# print('Done')
