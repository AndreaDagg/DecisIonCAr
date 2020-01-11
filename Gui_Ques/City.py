"""
Questa classe si occupa di effettuare le domande quando è stato scelto l'utilizzo in città.
Richiama la classe di Machine learning una volta settati tutti i parametri necessari.
"""

from tkinter import *
from PIL import ImageTk, Image


class City:

    def CityQuestion(self, frame):
        ColorBttn = "#BADEC0"
        ColorBttnTxtree = "#455a64"
        ColorBttnTxT = "#ff8f00"

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1230, height=660)
        imageN = ImageTk.PhotoImage(Image.open("img/DecisionCarCity.png"))
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=0, columnspan=5, rowspan=5)

        def Tree():
            from img.TreePng import ShowTree
            ShowTree(frame, "CITY")

        def PrintResult(value, q2, q3, q4, q5, q6):
            def db():
                from Dataset import Database
                Database.DatabaseConnection(value, "CITY", q2, q3, q4, q5, q6)

            def Home():
                from DecisionML import Decision
                Decision(frame)

            l1 = Label(frame, text="Ti consiglio di acquistare", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 50))
            b3 = Button(frame, text="Home", width=15, background=ColorBttn,
                        command=Home,
                        font=('Courrier', '15'),
                        foreground=ColorBttnTxtree)
            l3 = Label(frame, text=value, background='#c8e6c9', foreground="#e57373",
                       font=("Helvetica", 70))
            b1 = Button(frame, text="Visualizza Albero", width=15, background=ColorBttn,
                        command=Tree,
                        font=('Courrier', '15'),
                        foreground=ColorBttnTxtree)
            b2 = Button(frame, text="Caratteristiche", width=15, background=ColorBttn,
                        command=db,
                        font=('Courrier', '15'),
                        foreground=ColorBttnTxtree)

            l1.grid(row=0, column=4)
            b3.grid(row=4, column=4)
            l3.grid(row=1, column=4)
            b1.grid(row=2, column=4)
            b2.grid(row=3, column=4)

        def CallMachineLearnng(q1, q2, q3, q4, q5, q6):
            from Prediction import DecisionTreeCity
            predizione = DecisionTreeCity.DecisionML.Decison("self", q1, q2, q3, q4, q5, q6)
            PrintResult(predizione, q2, q3, q4, q5, q6)

        def Question1_6(q1, q2, q3, q4, q5):
            enterprice = StringVar(value="euro")

            def setPrice():
                ChoiceQ1_6 = enterprice.get()
                destryAll()
                CallMachineLearnng(q1, q2, q3, q4, q5, ChoiceQ1_6)

            l1 = Label(frame, text="Quale prezzo preferiresti?", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 50))
            insertPrice = Entry(frame, textvariable=enterprice, background="#e8f5e9", foreground=ColorBttnTxT,
                                font=("Helvetica", 30))
            l1.grid(row=0, column=4)
            insertPrice.grid(row=1, column=4)
            b3 = Button(frame, text="Inserisci", width=15, background=ColorBttn,
                        command=setPrice,
                        font=('Courrier', '20'),
                        foreground=ColorBttnTxT)

            b3.grid(row=2, column=4)

            def destryAll():
                l1.destroy()
                insertPrice.destroy()
                b3.destroy()

        def Question1_5(q1, q2, q3, q4):
            def setBenz():
                ChoiceQ1_5 = "BENZ"
                destryAll()
                Question1_6(q1, q2, q3, q4, ChoiceQ1_5)

            def setDis():
                ChoiceQ1_5 = "DIS"
                destryAll()
                Question1_6(q1, q2, q3, q4, ChoiceQ1_5)

            def setNotCarb():
                ChoiceQ1_5 = "NOTCARB"
                destryAll()
                Question1_6(q1, q2, q3, q4, ChoiceQ1_5)

            l1 = Label(frame, text="Quale tipo di carburante", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 60))
            l2 = Label(frame, text="preferisci?", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 50))

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

            l1 = Label(frame, text="Vuoi che sia potente?", background=ColorBttn, foreground="#43a047",
                       font=("Helvetica", 60))
            l2 = Label(frame, text="AdEs. Per trasportare merci", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 20))

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
                ChoiceQ1_2 = "Three"
                destryAll()
                Question1_3(q1, ChoiceQ1_2)

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

        Question1_2("citta")
        mainloop()

    def __init__(self, frame):
        frame.grid_forget()
        City.CityQuestion(self, frame)
