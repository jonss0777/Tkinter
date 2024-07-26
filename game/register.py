from clear import cleanWindow
def registerWindow(root, tk):
    cleanWindow(root)
    email_var = tk.StringVar()
    username_var = tk.StringVar()
    passw_var = tk.StringVar()

    register_label = tk.Label(root, text='Register', font=('calibre', 10, 'bold'))
    email_label = tk.Label(root, text='Email', font=('calibre', 10))
    email_entry = tk.Entry(root, textvariable=email_var ,fg="black", bg="brown", width=50)
    username_label = tk.Label(root, text='Username', font=('calibre', 10))
    username_entry = tk.Entry(root, textvariable= username_var, fg="black", bg="brown", width=50)
    passw_label = tk.Label(root, text='Password', font=('calibre', 10))
    passw_entry = tk.Entry(root, textvariable=passw_var,fg="black", bg="brown", width=50)

    login_button = tk.Button(root, text="Register", command=lambda:register(tk,email_var, username_var, passw_var))
    
    # Place widgets using grid with different rows and columns
    register_label.grid(row=0, column=0, padx=20, pady=10)
    email_label.grid(row=1, column=0, padx=20, pady=10)
    email_entry.grid(row=1, column=1, padx=20, pady=10)
    username_label.grid(row=2, column=0, padx=20, pady=10)
    username_entry.grid(row=2, column=1, padx=20, pady=10)
    passw_label.grid(row=3, column=0, padx=20, pady=10)
    passw_entry.grid(row=3, column=1, padx=20, pady=10)
    login_button.grid(row=3, column=2, padx=20, pady=10)

def register(tk,email_var, username_var, passw_var):
    print("Calling Register function")  
    print(email_var.get())
    print(username_var.get())
    print(passw_var.get())
    