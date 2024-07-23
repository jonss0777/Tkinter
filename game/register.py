from clear import cleanWindow
def registerWindow(root, tk):
    cleanWindow(root)
    register_label = tk.Label(root, text='Register', font=('calibre', 10, 'bold'))
    email_label = tk.Label(root, text='Email', font=('calibre', 10))
    email_entry = tk.Entry(root, fg="black", bg="brown", width=50)
    passw_label = tk.Label(root, text='Password', font=('calibre', 10))
    passw_entry = tk.Entry(root, fg="black", bg="brown", width=50)

    login_button = tk.Button(root, text="Register", command=lambda:register(tk,email_entry, passw_entry))
    

    # Place widgets using grid with different rows and columns
    register_label.grid(row=0, column=0, padx=20, pady=10)
    email_label.grid(row=1, column=0, padx=20, pady=10)
    email_entry.grid(row=1, column=1, padx=20, pady=10)
    passw_label.grid(row=2, column=0, padx=20, pady=10)
    passw_entry.grid(row=2, column=1, padx=20, pady=10)
    login_button.grid(row=2, column=2, padx=20, pady=10)

def register(tk,email_entry, passw_entry):
    print("You registered correctly!")
    email_var = tk.StringVar()
    passw_var = tk.StringVar()

    email_var = email_entry.get()
    passw_var = passw_entry.get()
    print(email_var)
    print(passw_var)