from tkinter import *
from src.music_widget import *
from tools.function import *
from src.gps_page import gps_page


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
            'text': 'Music',
            'command':lambda: music(window=window)
        },
        {
            'window': nav_bar,
            'text': 'Vitre',
            'command': None
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
