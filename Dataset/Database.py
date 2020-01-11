from tkinter import *
from PIL import ImageTk, Image
import MySQLdb


class DatabaseConnection:

    def DatabaseCall(self, frame, value, callBy):
        ColorBttn = "#c8e6c9"
        ColorBttnTxtree = "#455a64"
        ColorBttnTxT = "#ff8f00"

        def Home():
            from DecisionML import Decision
            Decision(frame)

        def Tree():
            if callBy == "CITY":
                from img.TreePng import ShowTree
                ShowTree(frame, "CITY")
            elif callBy == "TRIP":
                from img.TreePng import ShowTree
                ShowTree(frame, "TRIP")
            else:
                from img.TreePng import ShowTree
                ShowTree(frame, "RACE")

        frame.grid(row=0, column=0, columnspan=5, rowspan=5)

        db = MySQLdb.connect("127.0.0.1", "root", "", "cars")
        cursor = db.cursor()

        sqlSelect = 'SELECT MARCA,CARBURANTE,PORTE,CILINDRATA,CITTA,TRIP,PREZZO FROM tablecars WHERE MARCA = "' + value + '"'

        cursor.execute(sqlSelect)
        result = cursor.fetchall()

        l1 = Listbox(frame, width=200, height=660, fg=ColorBttnTxtree, font=('Comic Sans MS', 25))
        l1.insert(0, "modello,carburante,porte,cilindrata,mpgcitta,mpgautostrada,prezzo")
        for x in result:
            print(x)
            l1.insert(1, x)
        l1.grid(row=0, column=0)
        cursor.close()
        db.close()

        b1 = Button(frame, text="Visualizza Albero", width=15, background=ColorBttn,
                    command=Tree,
                    font=('Courrier', '10'),
                    foreground=ColorBttnTxtree)

        b2 = Button(frame, text="Home", width=15, background=ColorBttn,
                    command=Home,
                    font=('Courrier', '10'),
                    foreground=ColorBttnTxtree)
        b2.grid(row=2, col=1)
        b2.grid(row=2, col=3)

        mainloop()

    def __init__(self, frame, value, callBy):
        frame.grid_forget()
        DatabaseConnection.DatabaseCall(self, frame, value, callBy)
