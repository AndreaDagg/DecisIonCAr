from tkinter import *
from PIL import ImageTk, Image


class Main:

    def __init__(self):
        # pip install Pillow
        def canvasBuild():
            print("canvas call")
            canvas = Canvas(root, width=1280, height=720)
            image = ImageTk.PhotoImage(Image.open("DecisionCar.png"))
            canvas.create_image(0, 0, anchor=NW, image=image)
            canvas.grid(row=0, column=1, columnspan=3, rowspan="3")

        def changeImg():
            print("change image call")
            image = ImageTk.PhotoImage(Image.open("DecisionCar.png"))

        root = Tk()
        root.title("DecisionCar")
        root.geometry("1280x720")
        root.resizable(FALSE, FALSE)
        canvas = Canvas(root, width=1280, height=720)
        image = ImageTk.PhotoImage(Image.open("DecisionCar.png"))
        canvas.create_image(0, 0, anchor=NW, image=image)
        canvas.grid(row=0, column=1, columnspan=3, rowspan="3")

        l1 = Label(root, text="Benvenuto in", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 60))
        l2 = Label(root, text="decisIoncAr", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 90))

        l1.grid(row=0, column=3)
        l2.grid(row=1, column=3)

        b1 = Button(root, text="Start", command=changeImg, width=10, background="#c8e6c9", font=('Courrier', '50'),
                    foreground="#ff8f00")
        b1.grid(row=2, column=3)

        root.mainloop()
