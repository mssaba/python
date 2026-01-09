import tkinter as tk
from tkinter import *
r=Tk()
r.title("cinfig examole")
m=Label(r,text='hello world',bg='lightblue',fg='black',font=('Arial',15))
m.grid(row=0,column=1)


def change():
    m.config(text='button clicked',bg='yellow',fg='black',font=("Arial",17))

x=Button(r,text='Click me',command=change)
x.grid(row=1,column=1)
r.mainloop()