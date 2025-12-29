#format
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.title("sample")
# '''
# widgets

# '''
# root.mainloop()
'''
# Tkinter Widget

Label - The Label widget is used to provide a single-line caption for other widgets. It can also contain images.

Button - The Button widget is used to display the buttons in your application.

Entry - The Entry widget is used to display a single-line text field for accepting values from a user.

Text - The Text widget is used to display text in multiple lines.

Radiobutton - The Radiobutton widget is used to display a number of options as radio buttons. The user can select only one option at a time.

Checkbutton - The Checkbutton widget is used to display a number of options as checkboxes. The user can select multiple options at a time.

Combobox – walk you through the steps of creating a combobox widget.

Message - The Message widget is used to display multiline text fields for accepting values from a user.

Frame - The Frame widget is used as a container widget to organize other widgets.

Menu - The Menu widget is used to provide various commands to a user. These commands are contained inside Menubutton.

Menubutton - The Menubutton widget is used to display menus in your application. 

Canvas - The Canvas widget is used to draw shapes, such as lines, ovals, polygons and rectangles, in your application.
# '''
# #widgets
# #1.label
# import tkinter as tk
# from tkinter import ttk
# root = tk.Tk()
# root.title("Label Sample")

# label = tk.Label(root, text="Hello, World!")
# label.pack()
# root.mainloop()

# #2.button
# import tkinter as tk
# from tkinter import ttk
# root=tk.Tk()
# root.title('sample')

# b=tk.Button(root,text='stop',width=25,command=root.destroy)
# b.pack()
# root.mainloop()

#3.entry
# import tkinter as tk
# # from tkinter import ttk
# r=tk.Tk()
# r.title('sample')

# tk.Label(r, text='First Name').grid(row=0)
# tk.Label(r ,text='Last Name').grid(row=1)
# e1 = tk.Entry(r)
# e2 = tk.Entry(r)
# e1.grid(row=0, column=1)
# e2.grid(row=1, column=1)
# r.mainloop()

# #4.text
# from tkinter import*
# root=Tk()
# root.title("sample")

# T=Text(root,height=2,width=30)
# T.pack()
# mainloop()

#5.radiobutton runs both the button at the same time
# from tkinter import *
# r=Tk()
# r.title('buttons')

# v=IntVar()
# Radiobutton(r,text='yes',variable=v,value=1).pack(anchor=W)
# Radiobutton(r,text='no',variable=v,value=1).pack(anchor=W)
# mainloop()

#checkbutton
from tkinter import*
r=Tk()
r.title('button 2')
var1 = IntVar()
Checkbutton(r, text='male', variable=var1).grid(row=0, sticky=W)
var2 = IntVar()
Checkbutton(r, text='female', variable=var2).grid(row=1, sticky=W)
mainloop()