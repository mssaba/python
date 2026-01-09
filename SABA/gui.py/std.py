import tkinter as tk
from tkinter import *
from tkinter import ttk
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

c=ttk.Combobox(r,values=[ '1.abc engineering clg','2.xyz engineering clg','3.rst clg of engineering'])
c.grid(row=7,column=1)

def submit():
    a=(int(e4.get())+int(e5.get())+int(e6.get())+int(e7.get()))/4
    if(c.get()=='1.abc engineering clg'and 90<a<=100):
        m.config(text='you are elligible',fg='white',bg='blue',font=("Helvetica", 16, "bold"))
    elif(c.get()=='2.xyz engineering clg'and a>80):
         m.config(text='you are elligible',fg='white',bg='blue',font=("Helvetica", 16, "bold"))
    elif(c.get()=='3.rst clg of engineering'and a>70):
         m.config(text='you are elligible',fg='white',bg='blue',font=("Helvetica", 16, "bold"))
    else:
         m.config(text='you are not elligible',fg='white',bg='blue',font=("Helvetica", 16, "bold"))
         

m=Label(r ,text='')
m.grid(row=10,column=1)
button=Button(r,text='Check Elligibility ',width=30,command=submit)
button.grid(row=8,column=1)

def save():
     # file=open('save.txt','x')
     file=open('save.txt','a+')
     file.write("Name:"+e1.get()+"\n")
     file.write('Age:'+e2.get()+"\n")
     file.write('marks:'+e3.get()+"\n")
     file.write('Chemistry marks:'+e4.get()+"\n")   


button=Button(r,text='save',command=save)
button.grid(row=15,column=1)
r.mainloop()
