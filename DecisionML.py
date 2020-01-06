from tkinter import *
from PIL import ImageTk, Image
from MachineLearning.ML import MLStep1


class Decision:
    def newDecision(self, frame):
        print("New Frame")
        frame.grid(row=0, column=0, columnspan=3, rowspan=3)

        canvasN = Canvas(frame, width=1280, height=720)
        imageN = ImageTk.PhotoImage(Image.open("img/DecisionCar1.png"))
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=1, columnspan=3, rowspan=3)

        l1 = Label(frame, text="Per cosa utilizzerai", background='#c8e6c9', foreground="#43a047",
                   font=("Helvetica", 60))
        l2 = Label(frame, text="l'auto?", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 60))

        l1.grid(row=0, column=3)
        l2.grid(row=1, column=3)

        b1 = Button(frame, text="Answer", width=10, background="#c8e6c9",
                    command=MLStep1,
                    font=('Courrier', '50'),
                    foreground="#ff8f00")
        b1.grid(row=2, column=3)
        mainloop()

    def __init__(self, frame):
        frame.grid_forget()
        print("Clear Frame")
        Decision.newDecision(self, frame)
