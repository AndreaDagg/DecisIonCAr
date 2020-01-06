from tkinter import *
from PIL import ImageTk, Image

# pip install Pillow
from DecisionML import Decision


class StartPage():

    def __init__(self):
        root = Tk()
        root.title("DecisionCar")
        root.geometry("1280x720")
        root.resizable(FALSE, FALSE)
        icona = PhotoImage(file="img/DecisionCar.png")
        root.tk.call("wm", "iconphoto", root.w, icona)
        frame = Frame(root, height=1280, width=720)
        frame.grid(row=0, column=0, columnspan=3, rowspan=3)

        canvas = Canvas(frame, width=1280, height=720)
        image = ImageTk.PhotoImage(Image.open("img/DecisionCar.png"))
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.grid(row=0, column=1, columnspan=3, rowspan=3)

        l1 = Label(frame, text="Benvenuto in", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 60))
        l2 = Label(frame, text="decisIoncAr", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 90))

        l1.grid(row=0, column=3)
        l2.grid(row=1, column=3)

        def loadPage():
            Decision(frame)

        b1 = Button(frame, text="Start", command=loadPage, width=10, background="#c8e6c9",
                    font=('Courrier', '50'),
                    foreground="#ff8f00")
        b1.grid(row=2, column=3)

        root.mainloop()
