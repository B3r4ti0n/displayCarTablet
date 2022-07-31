from tkinter import *
from tools.function import *
from src.gps_page import gps_page
from src.music_widget import *


def create_nav_bar(window=None, width=0, heigth=0):
    nav_bar = Label(
        window,
        bg='grey',
        width=59,
        height=3
    )
    nav_bar.place(x=width, y=heigth)
    create_buttons_nav_bar([
        {
            'window': nav_bar,
            'text': 'GPS',
            'command': lambda: gps_page()
        },
        {
            'window': nav_bar,
            'text': 'Vitre',
            'command': None
        },
        {
            'window': nav_bar,
            'text': 'music',
            'command': lambda: music_widget(window, heigth*68.2666666667, width*25)
        },
        {
            'window': nav_bar,
            'text': 'Climatiseur',
            'command': None
        },
        {
            'window': nav_bar,
            'text': 'Paramêtre',
            'command': None
        },
    ])
