#!/usr/bin/env python
# ++++ HanSa - Hana's Screensaver ++++
# This script controls the main page aka the screensaver itself.

import lib.adaptive_element_sizes as aes
import lib.win_operations as wo
from tkinter import Tk, Label, Grid, Event, font


class main_page(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)
        result = False

        # Define standard values
        self.w = 500
        self.h = 300

        self.bg_color = "orange"

        wo.set_window_center(self, self.w, self.h)
        self.resizable(True, True)
        self.configure(bg = self.bg_color)

        # Specify Grid
        Grid.columnconfigure(self, index = 0, weight = 1)
        Grid.rowconfigure(self, 0,weight = 1)

        # Write some text into the window.
        self.font_type = 'Times New Roman bold'
        self.welc_text = "    "
        self.width_lockuptable = [[0, 0]]   # [width, recommended font size]
        self.height_lockuptable = [[0, 0]]   # [height, recommended font size]
        self.max_height_perc = 10      # max height of displyed tet with respect to the screen resolution [in percentage]
        self.max_width_perc = 90       # max width of displyed tet with respect to the screen resolution [in percentage]
        self.text_max_height = 0
        self.text_max_width = 0
        self.max_welc_text_size = 100  # start value of the font size (sizes cannot be larger than this)
        self.welc_text_size = self.max_welc_text_size      
        self.font_config = font.Font(font = (self.font_type, self.welc_text_size))

        result = aes.pick_text_size(self)

        if not result:
            self.label = Label(self, text = self.welc_text, font = self.font_config, bg = self.bg_color)
            self.label.grid(row = 0,column = 0,sticky = "N")
            self.label.pack(padx = 10, pady = 10)

            wo.resize_label(self)

            # Make it fullscreen
            # self.attributes('-fullscreen', True)

            self.bind("<Configure>", self.resize_handler)

            # Run the GUI.
            self.gui()

    def __enter__(self):
        return self

    def __exit__(self, exc_type, exc_value, exc_traceback):
        if exc_type:
            print(f"exc_type: {exc_type}")
            print(f"exc_value: {exc_value}")
            print(f"exc_traceback: {exc_traceback}")

    def resize_handler(self: Tk, event: Event) -> None:
        self.config(width=event.width, height=event.height)
        wo.resize_label(self)

    def gui(self) -> None:
        self.mainloop()
