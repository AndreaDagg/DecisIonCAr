from tkinter import *
from PIL import ImageTk, Image
from DecisionML import Decision
from Gui_Ques.City import City


class ShowTree:

    def show(self, frame, pathPng):
        ColorBttn = "#bdbdbd"
        ColorBttnTxtree = "#212121"

        def Home():
            Decision(frame)

        #frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1230, height=660)
        img = Image.open(pathPng)
        img = img.resize((1230, 660), Image.ANTIALIAS)
        imageN = ImageTk.PhotoImage(img)
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=0, columnspan=5, rowspan=5)

        bHome = Button(frame, text="Home", width=15, background=ColorBttn,
                       command=Home,
                       font=('Courrier', '10'),
                       foreground=ColorBttnTxtree)
        bHome.grid(row=4, column=2)
        mainloop()

    def __init__(self, frame, callBy):
        #frame.grid_forget()

        if callBy == "RACE":
            ShowTree.show(self, frame, "treerace.png")
        elif callBy == "TRIP":
            ShowTree.show(self, frame, "treetrip.png")
        elif callBy == "CITY":
            ShowTree.show(self, frame, "treecity.png")
        else:
            ShowTree.show(self, frame, "img/DecisionCar.png")
