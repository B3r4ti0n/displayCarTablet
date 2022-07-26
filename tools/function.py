import webbrowser

from tkinter import *
from tkinter import Button


def get_website(url):
    """
    show website
    :return: null
    """
    webbrowser.open(url)


def create_button(window=None, text=None, anchor='center', bg='gray', activeforeground='cyan', activebackground='grey',
                  command=None,
                  width=10, height=2):
    """
    create new button
    :param window: TK
    :param text: String
    :param anchor: String
    :param bg: String
    :param activeforeground: String
    :param activebackground: String
    :param width: Int
    :param height: Int
    :param command: Object
    :return: button: Button
    """

    button: Button = Button(
        window,
        text=text,
        anchor=anchor,
        bg=bg,
        activeforeground=activeforeground,
        activebackground=activebackground,
        command=command,
        width=width,
        height=height
    )
    return button


def create_buttons_nav_bar(buttons):
    """
    create most button for nav bar
    :param buttons:
    :return:
    """

    import tkinter.font as tk_font
    f = tk_font.Font(size=20)
    column = 0

    for button in buttons:
        button = create_button(
            window=button['window'],
            text=button['text'],
            command=button['command']
        )
        button['font'] = f
        button.grid(row=0, column=column)
        column += 1
