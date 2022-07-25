from tkinter import *
from src.gps_page import gps_page

# define an instance of tkinter
tk = Tk()
height = tk.winfo_screenheight()
width = tk.winfo_screenwidth()
#  size of the window where we show our website
tk.attributes('-fullscreen', True)

btn = Button(tk, text='GPS', command=gps_page(width, height))
btn.pack()

tk.mainloop()
