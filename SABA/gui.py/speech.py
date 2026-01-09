import tkinter as tk
import speech_recognition as a

def reg():
    reg=a.Recognizer
    with a.Microphone() as source:
        status_label.congif(text='listerning....')
        r.update()
        try:
            audio = reg.listen(source, timeout=5)
            text = reg.recognize_google(audio)
            result_text.set(text)
            status_label.config(text="Recognition complete.")
        except a.UnknownValueError:
            result_text.set("Could not understand audio.")
            status_label.config(text="Try again.")
        except a.RequestError:
            result_text.set("API unavailable.")
            status_label.config(text="Error.")

r=tk.Tk()
r.title('speech recognition')
r.geometry('400x200')
result_text= tk.StringVar()
tk.Label(r,text='click to speak',font=('Arial',41)).pack(pady=10)
tk.Button(r, text="Start Listening", command=reg).pack(pady=10)
tk.Label(r, textvariable=result_text, wraplength=350, font=("Arial", 12)).pack(pady=10)
status_label = tk.Label(r, text="", font=("Arial", 10), fg="blue")
status_label.pack()

r.mainloop()