from tkinter import *
import webview

# define an instance of tkinter
tk = Tk()

#  size of the window where we show our website
tk.attributes('-fullscreen', True)
height = tk.winfo_screenheight()

width = tk.winfo_screenwidth()
# Open website
#webview.create_window('GPS', 'https://www.google.com/maps/dir/?api=1&travelmode=driving', height=height, width=width)
#webview.start()

tk.mainloop()
