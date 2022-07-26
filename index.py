from tkinter import *
from tools.nav_bar import *

# define an instance of tkinter
tk = Tk()
height = tk.winfo_screenheight()
width = tk.winfo_screenwidth()

# size of the window where we show our website
tk.attributes('-fullscreen', True)

# setting to button to navigate in page
nav_bar = create_nav_bar(window=tk, width=width/51.2, heigth=height/25)

tk.mainloop()
