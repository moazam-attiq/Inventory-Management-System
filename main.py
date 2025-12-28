# main.py - FIX PYTHON PATH
import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from tkinter import Tk
from login import LoginWindow

root = Tk()
LoginWindow(root)
root.mainloop()
