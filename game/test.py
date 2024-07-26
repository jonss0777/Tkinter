import tkinter as tk

def show_frame1():
    frame2.pack_forget()
    frame1.pack()

def show_frame2():
    frame1.pack_forget()
    frame2.pack()

# Create the main window
root = tk.Tk()
root.title("Tkinter Navigation Example")

# Create frames
frame1 = tk.Frame(root)
frame2 = tk.Frame(root)

# Frame 1 contents
tk.Label(frame1, text="This is Frame 1").pack()
tk.Button(frame1, text="Go to Frame 2", command=show_frame2).pack()

# Frame 2 contents
tk.Label(frame2, text="This is Frame 2").pack()
tk.Button(frame2, text="Back to Frame 1", command=show_frame1).pack()

# Start with Frame 1
show_frame1()

root.mainloop()


