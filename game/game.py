# Requirements:
# Snake game
# with shared global score board stored in MongoDB

from main import mainWindow
from display import displayGame
import tkinter as tk 

frames = {"MAIN": None,"REGISTER": None, "LOGIN": None}

root = tk.Tk()
frames["MAIN"] = tk.Frame(root)
frames["REGISTER"]  = tk.Frame(root)
frames["LOGIN"] = tk.Frame(root)

root.title("Santa Snake")
root.geometry("600x400")
states = {"menu": 0, "pauseGame": 1, "playingGame":3}
mainWindow(tk, frames)
root.mainloop()