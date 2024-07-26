
from PIL import Image, ImageTk
import os


def objectCheckBounds(dx, dy, cx, cy, paddingWidth, paddingHeight):
    if not (cy - paddingHeight >= 0 and cy +  paddingHeight<= dy):
        print("Outside")
    if not (cx - paddingWidth >= 0 and cx + paddingHeight<= dx):
        print("Outside")

def displayGame(tk, root):
    w = 500
    h = 400
    canvas = tk.Canvas(root, width=w, height=h, background='blue')
    canvas.pack()

    def savePosn(event):
        global lastx, lasty
        lastx, lasty = event.x, event.y

    def draw(event):
        image_path = os.path.join(os.path.dirname(__file__), '../img/oso.png')
        img = ImageTk.PhotoImage(Image.open(image_path))
        canvas.image = img
        canvas.create_image(event.x, event.y,anchor=tk.CENTER, image=img)
        objectCheckBounds(w, h, event.x, event.y, img.height()//2, img.height()//2)
        savePosn(event)
    
    canvas.grid(column=0, row=0, sticky=(tk.N, tk.W, tk.E, tk.S))
    canvas.bind("<Button-1>", savePosn)
    canvas.bind("<B1-Motion>", draw)