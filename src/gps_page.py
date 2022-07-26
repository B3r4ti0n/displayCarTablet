from tkinter import *
import tools.function as f


def gps_page():
    """
    show page of gps with google maps
    :return:
    """
    f.get_website('https://www.google.com/maps/dir/?api=1&travelmode=driving')
