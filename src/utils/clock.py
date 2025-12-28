# utils/clock.py
import time
from tkinter import Label

def format_time():
    time_ = time.strftime("%I:%M:%S")
    date_ = time.strftime("%d-%m-%Y")
    return f"Welcome to Inventory Management System\t\t Date: {date_}\t\t Time: {time_}"

def setup_clock(label: Label, delay=200):
    """**Duplicated Code (13)** → Shared utility"""
    def update():
        label.config(text=format_time())
        label.after(delay, update)
    update()
