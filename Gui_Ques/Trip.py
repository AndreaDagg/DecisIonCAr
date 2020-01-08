"""
Questa classe si occupa di effettuare le domande quando è stato scelto l'utilizzo in viaggio.
Richiama la classe di Machine learning una volta settati tutti i parametri necessari.
"""

from tkinter import *
from PIL import ImageTk, Image


class Trip:

    def TripQuestion(self, frame):
        ColorBttn = "#c8e6c9"
        ColorBttnTxtree = "#455a64"
        ColorBttnTxT = "#ff8f00"

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1280, height=720)
        imageN = ImageTk.PhotoImage(Image.open("img/DecisionCarTripp.png"))
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=0, columnspan=5, rowspan=5)

        def Tree():
            from TreePng import ShowTree
            ShowTree(frame, "city")

        def PrintResult(value):
            l1 = Label(frame, text="Ti consiglio di cercare un auto", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 50))
            l2 = Label(frame, text="di questa marca:", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 40))
            l3 = Label(frame, text=value, background='#c8e6c9', foreground="#e57373",
                       font=("Helvetica", 70))
            b1 = Button(frame, text="Visualizza Albero", width=15, background=ColorBttn,
                        command=Tree,
                        font=('Courrier', '10'),
                        foreground=ColorBttnTxtree)

            l1.grid(row=0, column=4)
            l2.grid(row=1, column=4)
            l3.grid(row=2, column=4)
            b1.grid(row=4, column=4)

        def CallMachineLearnng(q1, q2, q3, q4, q5):
            from MachineLearning import DecisionTreeTrip
            predictTrip = DecisionTreeTrip.DecisionML.Decison("self", q1, q2, q3, q4, q5)
            PrintResult(predictTrip)

        def Question1_5(q1, q2, q3, q4):
            def setBenz():
                ChoiceQ1_5 = "BENZ"
                destryAll()
                CallMachineLearnng(q1, q2, q3, q4, ChoiceQ1_5)

            def setDis():
                ChoiceQ1_5 = "DIS"
                destryAll()
                CallMachineLearnng(q1, q2, q3, q4, ChoiceQ1_5)

            def setNotCarb():
                ChoiceQ1_5 = "NOTCARB"
                destryAll()
                CallMachineLearnng(q1, q2, q3, q4, ChoiceQ1_5)

            l1 = Label(frame, text="Quale tipo di carburante preferisci?", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 45))
            l2 = Label(frame, text="Per lunghi tragitti consiglio Diesel", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 20))

            l1.grid(row=0, column=4)
            l2.grid(row=1, column=4)
            b1 = Button(frame, text="Benzina", width=15, background=ColorBttn,
                        command=setBenz,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b2 = Button(frame, text="Diesel", width=15, background=ColorBttn,
                        command=setDis,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b3 = Button(frame, text="Salta", width=15, background=ColorBttn,
                        command=setNotCarb,
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

        def Question1_4(q1, q2, q3):
            def setAnt():
                ChoiceQ1_4 = "ANT"
                destryAll()
                Question1_5(q1, q2, q3, ChoiceQ1_4)

            def setPost():
                ChoiceQ1_4 = "POST"
                destryAll()
                Question1_5(q1, q2, q3, ChoiceQ1_4)

            def setNot():
                ChoiceQ1_4 = "NOT"
                destryAll()
                Question1_5(q1, q2, q3, ChoiceQ1_4)

            l1 = Label(frame, text="Quale tipo di trazione", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 60))
            l2 = Label(frame, text="preferisci?", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 50))

            l1.grid(row=0, column=4)
            l2.grid(row=1, column=4)
            b1 = Button(frame, text="Anterirore", width=15, background=ColorBttn,
                        command=setAnt,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b2 = Button(frame, text="Posteriore", width=15, background=ColorBttn,
                        command=setPost,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b3 = Button(frame, text="Salta", width=15, background=ColorBttn,
                        command=setNot,
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

        def Question1_3(q1, q2):
            def setYes():
                ChoiceQ1_3 = True
                destryAll()
                Question1_4(q1, q2, ChoiceQ1_3)

            def setNo():
                ChoiceQ1_3 = False
                destryAll()
                Question1_4(q1, q2, ChoiceQ1_3)

            l1 = Label(frame, text="Preferisci un auto", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 60))
            l2 = Label(frame, text="familiare?", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 50))

            l1.grid(row=0, column=4)
            l2.grid(row=1, column=4)
            b1 = Button(frame, text="Si", width=15, background=ColorBttn,
                        command=setYes,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b2 = Button(frame, text="No", width=15, background=ColorBttn,
                        command=setNo,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b1.grid(row=2, column=4)
            b2.grid(row=3, column=4)

            def destryAll():
                l1.destroy()
                l2.destroy()
                b1.destroy()
                b2.destroy()

        def Question1_2(q1):
            def setThree():
                '''
                Se seleziono 2 porte non domando se familiare
                '''
                ChoiceQ1_2 = "Three"
                destryAll()
                Question1_4(q1, ChoiceQ1_2, FALSE)

            def setFive():
                ChoiceQ1_2 = "Five"
                destryAll()
                Question1_3(q1, ChoiceQ1_2)

            l1 = Label(frame, text="Quante porte preferisci?", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 60))
            l1.grid(row=0, column=4)
            b1 = Button(frame, text="Tre", width=15, background=ColorBttn,
                        command=setThree,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b2 = Button(frame, text="Cinque", width=15, background=ColorBttn,
                        command=setFive,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b1.grid(row=2, column=4)
            b2.grid(row=3, column=4)

            def destryAll():
                l1.destroy()
                b1.destroy()
                b2.destroy()

        Question1_2("trip")
        mainloop()

    def __init__(self, frame):
        frame.grid_forget()
        Trip.TripQuestion(self, frame)
