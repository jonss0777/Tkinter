
from login import loginWindow
from register import registerWindow
def mainWindow(root, tk):
    title_label = tk.Label(root, text='SantaSnake', font=('calibre', 10, 'bold'))
    login_btn = tk.Button(root, text='Login', command=lambda: loginWindow(root, tk))
    register_tbn = tk.Button(root, text='Login', command=lambda: registerWindow(root, tk) )
    # Place the title label in row 0, column 0
    title_label.grid(row=0, column=0, padx=250, pady=10)

    # Place the login button in row 1, column 0
    login_btn.grid(row=1, column=0, padx=250, pady=10)
    register_tbn.grid(row=2, column=0, padx=250, pady=10)

