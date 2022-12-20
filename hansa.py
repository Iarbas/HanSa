#!/usr/bin/env python
# ++++ HanSa - Hana's Screensaver ++++
# This small program replaces some functionalities of the Windows account manager for children.
# It serves as a time controller (when and how long) for children - assumed that the child account
# has no admin rights.
# In addition the program gives task to the child each x minutes and releases the periphery and
# screen after solving x math equations with adaptive difficulty levels.

import lib.win_operations as wo
import pages.main_page as mp
import sys


def Hansa() -> None:

    with mp.main_page() as screensaver:
        print("Exiting...")


def main():

    print("\n\n#################################################################")
    print("Starting: HanSa - the screensaver to manage your child's PC time.")
    print("#################################################################\n\n")

    Hansa()

    sys.exit()


if __name__ == "__main__":
    main()
