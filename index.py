from tkinter import *
import tkinter.font as font
from src.gps_page import gps_page

# define an instance of tkinter
tk = Tk()
height = tk.winfo_screenheight()
width = tk.winfo_screenwidth()

# size of the window where we show our website
tk.attributes('-fullscreen', True)

# setting to button to navigate in page
f = font.Font(size=20)
width_button = 10
height_button = 2
position_start_x = 3
position_start_y = 4

# label to contain buttons
#nav_bar = Label(
 #   tk,
 #   bg='grey',
 #   width=59,
 #   height=3
#)
#nav_bar.place(x=width/7, y=position_start_y+100)
# button to show gps
gps = Button(
    tk,
    text=height,
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    command=lambda: gps_page(width, height, tk),
    width=width_button,
    height=height_button
)
gps['font'] = f
gps.grid(row=1,column=1)
position_start_x += 100

# button to show settings
settings = Button(
    tk,
    text=width,
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
settings['font'] = f
settings.grid(row=1,column=2)
position_start_x += 110

# button to show air conditioner settings
air_cond = Button(
    tk,
    text='Clime',
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
air_cond['font'] = f
air_cond.grid(row=1,column=3)
position_start_x += 100

# button to show glass pane controller panel
glass_pane = Button(
    tk,
    text='Vitre',
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
glass_pane['font'] = f
glass_pane.grid(row=1,column=4)
position_start_x += 100

# button to show music controller panel
sound = Button(
    tk,
    text='Music',
    anchor='center',
    bg='grey',
    activeforeground='cyan',
    activebackground='grey',
    width=width_button,
    height=height_button
)
sound['font'] = f
sound.grid(row=1,column=5)
tk.mainloop()
