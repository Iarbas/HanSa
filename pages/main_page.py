#!/usr/bin/env python
# ++++ HanSa - Hana's Screensaver ++++
# This script controls the main page aka the screensaver itself.

import lib.win_operations as wo
from tkinter import Tk, Label


class main_page(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)
        # Define standard values
        self.w = 500
        self.h = 300
        wo.set_window_center(self, self.w, self.h)
        self.resizable(False, False)

        # Write some text into the window.
        label= Label(self, text= "Hello child, your screensaver activated.", font=('Times New Roman bold',20))
        label.pack(padx=10, pady=10)

        # Make it fullscreen
        self.attributes('-fullscreen', True)

        # Run the GUI.
        self.gui()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"exc_type: {exc_type}")
            print(f"exc_value: {exc_value}")
            print(f"exc_traceback: {exc_traceback}")

    def gui(self) -> None:
        self.mainloop()
