def show_loginWindow(frames):
    frames["MAIN"].pack_forget()
    frames["REGISTER"].pack_forget()
    frames["LOGIN"].pack()

def show_mainWindow(frames):
    frames["MAIN"].pack()
    frames["REGISTER"].pack_forget()
    frames["LOGIN"].pack_forget() 

def loginWindow(tk, frames):
    loginFrame = frames["LOGIN"]

    email_var = tk.StringVar()
    username_var = tk.StringVar()
    passw_var = tk.StringVar()
    
    login_label = tk.Label(loginFrame, text='Login', font=('calibre', 10, 'bold'))
    email_label = tk.Label(loginFrame, text='Email', font=('calibre', 10))
    email_entry = tk.Entry(loginFrame, textvariable=email_var,fg="black", bg="brown", width=50)
    username_label = tk.Label(loginFrame, text='Username', font=('calibre', 10))
    username_entry = tk.Entry(loginFrame,textvariable=username_var, fg="black", bg="brown", width=50)
    passw_label = tk.Label(loginFrame, text='Password', font=('calibre', 10))
    passw_entry = tk.Entry(loginFrame, textvariable=passw_var,fg="black", bg="brown", width=50)

    login_button = tk.Button(loginFrame, text="Login", command=lambda:login(email_var, username_var, passw_var))  

    return_button = tk.Button(loginFrame, text="Return", command=lambda:show_mainWindow(frames))  

    # Place widgets using grid with different rows and columns
    login_label.grid(row=0, column=0, padx=20, pady=10)
    email_label.grid(row=1, column=0, padx=20, pady=10)
    email_entry.grid(row=1, column=1, padx=20, pady=10)
    username_label.grid(row=2, column=0, padx=20, pady=10)
    username_entry.grid(row=2, column=1, padx=20, pady=10)
    passw_label.grid(row=3, column=0, padx=20, pady=10)
    passw_entry.grid(row=3, column=1, padx=20, pady=10)
    login_button.grid(row=3, column=2, padx=20, pady=10)
    return_button.grid(row=4, column=0, padx=20, pady=10)

    show_loginWindow(frames)

def login(email_var, username_var,passw_var):
    print("Calling login function")
    print(email_var.get())
    print(username_var.get())
    print(passw_var.get())
    