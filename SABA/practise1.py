import tkinter as tk
from tkinter import *
r=Tk()
r.title('sample')

Label(r, text='enter Name').grid(row=0)
Label(r ,text='enter age').grid(row=1)
Label(r, text='enter ur mark').grid(row=2)
Label(r ,text='enter chemistry mark').grid(row=3)
Label(r, text='enter maths mark').grid(row=4)
Label(r ,text='enter physics mark').grid(row=5)
Label(r ,text='enter computer science mark').grid(row=6)
e1 = Entry(r)
e2 = Entry(r)
e3 = Entry(r)
e4 = Entry(r)
e5 = Entry(r)
e6 = Entry(r)
e7 = Entry(r)
e1.grid(row=0, column=1)
e2.grid(row=1, column=1)
e3.grid(row=2, column=1)
e4.grid(row=3, column=1)
e5.grid(row=4, column=1)
e6.grid(row=5, column=1)
e7.grid(row=6, column=1)

def save():
     file=open('save.csv','x')
     file=open('save.csv','a+')
     file.write("Name:"+e1.get()+"\n")
     file.write('Age:'+e2.get()+"\n")
     file.write('marks:'+e3.get()+"\n")
     file.write('Chemistry marks:'+e4.get()+"\n")   

m=Label(r ,text='')
m.grid(row=10,column=1)
button=Button(r,text='save ',width=30,command=save)
button.grid(row=8,column=1)

def clear():
         file=open('save.csv','w')
n=Label(r ,text='')
m.grid(row=15,column=1)
button=Button(r,text='clear ',width=30,command=clear)
button.grid(row=10,column=1)

r.mainloop()