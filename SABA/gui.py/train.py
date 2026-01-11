import tkinter as tk
from tkinter import*

r = Tk()
r.title("Canvas Demo")
canvas = Canvas(r, width=800, height=600, bg="white")
canvas.pack()
a=[]
a.append(canvas.create_rectangle(300, 300, 500, 400, outline="green", fill="lightgreen"))
a.append(canvas.create_oval(310,405,340,435, outline="green", fill="red"))
a.append(canvas.create_oval(485,405,455,435, outline="green", fill="red"))

def move():
    for i in a:
        canvas.move(i,30,0)
    canvas.after(10,move)
move()
r.mainloop()