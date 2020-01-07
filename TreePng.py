from tkinter import *
from PIL import ImageTk, Image
from DecisionML import Decision
from Gui_Ques.City import City


class ShowTree:

    def showCity(self, frame):
        ColorBttn = "#bdbdbd"
        ColorBttnTxtree = "#212121"

        def Home():
            Decision(frame)

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1280, height=720)
        img = Image.open("treecity.png")
        img = img.resize((1280, 720), Image.ANTIALIAS)
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
        frame.grid_forget()
        switcher = {
            "city": ShowTree.showCity(self, frame)
        }
        switcher.get(callBy, "Invalid call")
