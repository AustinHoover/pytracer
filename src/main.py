#!/usr/bin/env python3
"""
Main entry point for the pytracer desktop application.
"""
from tkinter import *
from window import Window


def main() -> None:
    window = Window()
    window.start()



if __name__ == "__main__":
    main()
