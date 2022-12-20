#!/usr/bin/env python
# ++++ HanSa Configurator ++++
# This script controls the GUI to configure the settings.

import lib.win_operations as wo
from tkinter import Tk


class gui_main_page(Tk):
    def __init__(self) -> None:
        Tk.__init__(self)
        # Define standard values
        self.w = 500
        self.h = 300
        wo.set_window_center(self, self.w, self.h)
        self.resizable(False, False)

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
