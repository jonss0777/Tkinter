# Requirements:
# Snake game
# with shared global score board stored in MongoDB

from main import mainWindow
from display import displayGame
import tkinter as tk 


root = tk.Tk()
root.title("Santa Snake")
root.geometry("600x400")


states = {"menu": 0, "pauseGame": 1, "playingGame":3}

displayGame(tk,root)
root.mainloop()