from tkinter import *
from PIL import ImageTk, Image

# pip install Pillow


root = Tk()
canvas = Canvas(root, width=1280, height=720)
image = ImageTk.PhotoImage(Image.open("DecisionCar.png"))

canvas.create_image(0, 0, anchor=NW, image=image)

canvas.grid(row=0, column=1)

l1 = Label(root, text="ciao", background='black', foreground="white")

l1.grid(row=0, column=1)

root.mainloop()
