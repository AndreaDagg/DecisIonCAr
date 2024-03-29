from tkinter import *
from PIL import ImageTk, Image

# pip install Pillow
from DecisionML import Decision


class StartPage:

    def __init__(self):
        root = Tk()
        root.title("DecisionCar")
        root.geometry("1230x660")
        root.resizable(FALSE, FALSE)
        icona = PhotoImage(file="img/iconDCc.png")
        root.tk.call("wm", "iconphoto", root._w, icona)
        frame = Frame(root, height=660, width=1230)
        frame.grid(row=0, column=0, columnspan=5, rowspan=6)

        canvas = Canvas(frame, width=1280, height=660)
        image = ImageTk.PhotoImage(Image.open("img/DecisionCarsStart.png"))
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.grid(row=0, column=1, columnspan=5, rowspan=6)

        def loadPage():
            Decision(frame)

        b1 = Button(frame, text="Start", command=loadPage, width=10, background="#BADEC0",
                    font=('Courrier', '40'),
                    foreground="#ff8f00")
        b1.grid(row=4, column=4)

        root.mainloop()
