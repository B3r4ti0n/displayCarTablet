from tkinter import *
import webview


def get_website(name, url, width, height):
    """
    show website
    :return: null
    """
    webview.create_window(name, url, height=height,
                          width=width)
    webview.start()
