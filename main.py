import tkinter as tk
import gui
import pi

# ROOM = "50_milk_women_1"
ROOM = "50_milk_women_2"
USE_GUI = 1

if USE_GUI:
    gui.init(ROOM)
else:
    print("USE_PI")