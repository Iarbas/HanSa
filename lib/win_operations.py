#!/usr/bin/env python

from tkinter import Tk


def set_window_center(window: Tk, width: float, height: float) -> None:

    w_s = window.winfo_screenwidth()
    h_s = window.winfo_screenheight()

    x_co = (w_s - width) / 2
    y_co = (h_s - height) / 2 - 50
    window.geometry("%dx%d+%d+%d" % (width, height, x_co, y_co))
    window.minsize(width, height)


def get_screen_size(window: Tk) -> None:
    return window.winfo_screenwidth(), window.winfo_screenheight()


def get_window_size(window: Tk) -> None:
    return window.winfo_width(), window.winfo_height()

def resize_label(window: Tk) -> None:
    [window_width, window_height] = get_window_size(window)

    