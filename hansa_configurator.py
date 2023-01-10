#!/usr/bin/env python
# ++++ HanSa Configurator ++++
# This small GUI helps parents to configure the screensaver settings.
# TODO: Name all possible settings and explain them.

import pages.configurator_page as cp
import sys


def Hansa() -> None:

    with cp.gui_main_page() as configurator:
        print("Exiting...")


def main():

    print("\n\n#################################################################")
    print("Starting: HanSa Configurator.")
    print("#################################################################\n\n")

    Hansa()

    print("Exiting...")

    sys.exit()


if __name__ == "__main__":
    main()