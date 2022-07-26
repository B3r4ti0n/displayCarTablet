from tkinter import *
import tkinter.font as font
from src.gps_page import gps_page
import webview

# define an instance of tkinter
tk = Tk()
height = tk.winfo_screenheight()
width = tk.winfo_screenwidth()

# size of the window where we show our website
tk.attributes('-fullscreen', True)

# setting to button to navigate in page
f = font.Font(size=30)
width_button = 10
height_button = 2
position_start_x = 0
position_start_y = 0

# label to contain buttons
nav_bar = Label(
    tk,
    bg='grey',
    width=114,
    height=5
)
nav_bar.place(x=width/7, y=position_start_y+100)
# button to show gps
gps = Button(
    nav_bar,
    text='GPS',
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    command=lambda: gps_page(width, height, tk),
    width=width_button,
    height=height_button
)
gps['font'] = f
gps.place(x=0, y=0)
position_start_x += 200

# button to show settings
settings = Button(
    nav_bar,
    text='Settings',
    anchor='center',
    bg='blue',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
settings['font'] = f
settings.place(x=position_start_x, y=position_start_y)
position_start_x += 200

# button to show air conditioner settings
air_cond = Button(
    nav_bar,
    text='Climatiseur',
    anchor='center',
    bg='blue',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
air_cond['font'] = f
air_cond.place(x=position_start_x, y=position_start_y)
position_start_x += 200

# button to show glass pane controller panel
glass_pane = Button(
    nav_bar,
    text='Vitre',
    anchor='center',
    bg='blue',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
glass_pane['font'] = f
glass_pane.place(x=position_start_x, y=position_start_y)
position_start_x += 200

# button to show music controller panel
sound = Button(
    nav_bar,
    text='Music',
    anchor='center',
    bg='blue',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
sound['font'] = f
sound.place(x=position_start_x, y=position_start_y)
tk.mainloop()
