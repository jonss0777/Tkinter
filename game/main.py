
from login import loginWindow
from register import registerWindow

def show_mainWindow(frames):
    frames["MAIN"].pack()
    frames["REGISTER"].pack_forget()
    frames["LOGIN"].pack_forget()

def mainWindow(tk, frames):
    mainFrame = frames["MAIN"]
    
    title_label = tk.Label(mainFrame, text='SantaSnake', font=('calibre', 10, 'bold'))
    login_btn = tk.Button(mainFrame, text='Login', command=lambda: loginWindow(tk,frames))
    register_tbn = tk.Button(mainFrame, text='Register', command=lambda: registerWindow(tk, frames) )

    # Place the title label in row 0, column 0
    title_label.grid(row=0, column=0, padx=250, pady=10)
    # Place the login button in row 1, column 0
    login_btn.grid(row=1, column=0, padx=250, pady=10)
    register_tbn.grid(row=2, column=0, padx=250, pady=10)
    show_mainWindow(frames)

    