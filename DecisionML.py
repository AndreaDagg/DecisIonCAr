from tkinter import *
from PIL import ImageTk, Image
from MachineLearning.ML import MLStep1


class Decision:

    def newDecision(self, frame):
        ColorBttn = "#c8e6c9"
        ColorBttnTxT = "#ff8f00"

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        canvasN = Canvas(frame, width=1280, height=720)
        imageN = ImageTk.PhotoImage(Image.open("img/DecisionCar1.png"))
        canvasN.create_image(0, 0, anchor=NW, image=imageN)
        canvasN.grid(row=0, column=0, columnspan=5, rowspan=5)

        def CallMachineLearnng(q1, q2, q3, q4, q5):
            # print(ChoiceQ1 + " " + ChoiceQ1_2 + " " + ChoiceQ1_3 + " " + ChoiceQ1_4 + " " + ChoiceQ1_5)
            print(q1 + " " + q2 + " " + " " + q4 + " " + q5)
            from MachineLearning import DecisionThreeML
            DecisionThreeML.DecisionML(q1, q2, q3, q4, q5)

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

        def Question1():
            def setCitta():
                ChoiceQ1 = "citta"
                destryAll()
                Question1_2(ChoiceQ1)

            def setViaggiare():
                ChoiceQ1 = "viaggio"
                destryAll()
                Question1_2(ChoiceQ1)

            def setSvago():
                ChoiceQ1 = "svago"
                destryAll()
                Question1_2(ChoiceQ1)

            l1 = Label(frame, text="Per cosa utilizzerai", background='#c8e6c9', foreground="#43a047",
                       font=("Helvetica", 60))
            l2 = Label(frame, text="l'auto?", background='#c8e6c9', foreground="#43a047", font=("Helvetica", 50))

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

            b3 = Button(frame, text="Svago", width=15, background=ColorBttn,
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
