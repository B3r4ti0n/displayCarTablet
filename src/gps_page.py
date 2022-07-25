from tkinter import *
import tools.function as f


def gps_page(width, height):
    """
    show page of gps with google maps
    :return:
    """
    f.get_website('name', 'https://www.google.com/maps/dir/?api=1&travelmode=driving', width, height)
