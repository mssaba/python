# from tkinter import *
# from PIL import Image, ImageTk

# root=Tk()
# root.title("Image")
# root.geometry("600x400")

# bg_image=Image.open("eagle.jpg")
# bg_photo=ImageTk.PhotoImage(bg_image.resize((600,400)))

# bg_label=Label(root,image=bg_photo)
# bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# b=Button(bg_label,text="Submit")
# b.pack(padx=300,pady=300)
# root.mainloop()



#image as button
# import tkinter as tk
# from PIL import Image, ImageTk

# root=tk.Tk()
# root.title('image as button')

# image1=Image.open('eagle.jpg')
# image=ImageTk.PhotoImage(image1.resize((100,50)))

# image_button=tk.Button(root, image=image)
# image_button.pack()
# root.mainloop()

#tkinter image
# import tkinter as tk
# from tkinter import PhotoImage
# root=tk.Tk()
# root.title("Adding Image")

# image=PhotoImage(file='eagle.jpg')
# image_label = tk.Label(root, image=image)
# image_label.pack()

# root.mainloop()

import tkinter as tk
from tkinter import messagebox
import qrcode
from PIL import Image,ImageTk

def gen_QR():
    d=e.get()
    if not d:
        messagebox.showwarning('input error', 'Please enter some text to generate QR')
        return
    qr=qrcode.QRCode(version=1,box_size=10,border=5)
    qr.add_data(d)
    qr.make(fit=True)

    img=qr.make_image(fill_color='black',back_color='white')
    img=img.resize((400,400))
    
    img_tk = ImageTk.PhotoImage(img)
    qr_label.config(image=img_tk)
    qr_label.image = img_tk  # Keep reference to avoid garbage collection


root = tk.Tk()
root.title("QR Code Generator")

tk.Label(root, text="Enter text or URL:").pack(pady=5)
e = tk.Entry(root, width=40)
e.pack(pady=5)

tk.Button(root, text="Generate QR Code", command=gen_QR).pack(pady=10)

qr_label = tk.Label(root)
qr_label.pack(pady=10)

root.mainloop()
     