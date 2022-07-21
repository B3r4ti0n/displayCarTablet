from tkinter import *
from tkinter import ttk


windows = Tk()
windows.attributes('-fullscreen', True)
label = Label(windows, text="Hello World")
label.pack()

windows.mainloop()