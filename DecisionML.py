from tkinter import *
from PIL import ImageTk, Image
from Gui_Ques.City import City
from Gui_Ques.Trip import Trip
from Gui_Ques.Race import Race


class Decision:

    def newDecision(self, frame):
        ColorBttn = "#c8e6c9"
        ColorBttnTxT = "#ff8f00"

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1230, height=660)
        imageN = ImageTk.PhotoImage(Image.open("img/DecisionCar1.png"))
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=0, columnspan=5, rowspan=6)

        def Question1():
            def setCitta():
                ChoiceQ1 = "citta"
                destryAll()
                # Question1_2(ChoiceQ1)
                City(frame)

            def setViaggiare():
                ChoiceQ1 = "viaggio"
                destryAll()
                # Question1_2(ChoiceQ1)
                Trip(frame)

            def setSvago():
                ChoiceQ1 = "svago"
                destryAll()
                # Question1_2(ChoiceQ1)
                Race(frame)

            l1 = Label(frame, text="Per cosa utilizzerai", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 70))
            l2 = Label(frame, text="l'auto?", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 60))

            l1.grid(row=0, column=4)
            l2.grid(row=1, column=4)

            b1 = Button(frame, text="Spostarmi in Città", width=15, background=ColorBttn,
                        command=setCitta,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b2 = Button(frame, text="Viaggiare", width=15, background=ColorBttn,
                        command=setViaggiare,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b3 = Button(frame, text="Entrambi ", width=15, background=ColorBttn,
                        command=setSvago,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)
            b1.grid(row=2, column=4)
            b2.grid(row=3, column=4)
            b3.grid(row=4, column=4)

            def destryAll():
                l1.destroy()
                l2.destroy()
                b1.destroy()
                b2.destroy()
                b3.destroy()

        Question1()
        mainloop()

    def __init__(self, frame):
        frame.grid_forget()
        Decision.newDecision(self, frame)
