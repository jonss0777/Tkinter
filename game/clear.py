def cleanWindow(root):
    listOfChildren = root.winfo_children()
    for widget in listOfChildren:
        #print(widget)
        widget.destroy()
