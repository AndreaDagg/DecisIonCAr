from tkinter import *
from PIL import ImageTk, Image
import MySQLdb


class DatabaseConnection:

    def DatabaseCall(self, value, callBy, q2, q3, q4, q5, q6):
        ColorBttn = "#c8e6c9"
        ColorBttnTxtree = "#455a64"
        ColorBttnTxT = "#ff8f00"

        rootDB = Tk()
        rootDB.title("Caratteristiche")
        rootDB.geometry("800x400")
        rootDB.resizable(FALSE, FALSE)

        db = MySQLdb.connect("127.0.0.1", "root", "", "cars")
        cursor = db.cursor()

        sqlSelect = 'SELECT MARCA,CARBURANTE,PORTE,CILINDRATA,CITTA,TRIP,PREZZO FROM tablecars WHERE MARCA = "' + value + '"'

        cursor.execute(sqlSelect)
        result = cursor.fetchall()

        l1 = Listbox(rootDB,height=10,width=150, bg="#cfd8dc", fg = ColorBttnTxtree, font = ('Comic Sans MS', 18))
        l1.insert(0, "modello,carburante,porte,cilindrata,mpgcitta,mpgautostrada,prezzo")
        for x in result:
            #print(x)
            l1.insert(1, x)

        sqlInsert = 'INSERT INTO predictions (MARCA,Q1,Q2,Q3,Q4,Q5,Q6,TIPO) VALUES ("' + value + '","C","' + q2 + '","' + str(
            q3) + '","' + q4 + '","' + q5 + '","' + q6 + '","' + callBy + '")'
        cursor.execute(sqlInsert)
        db.commit()

        cursor.close()
        db.close()

        l1.grid(row=0, column=1)

        mainloop()

    def __init__(self, value, callBy, q2, q3, q4, q5, q6):
        DatabaseConnection.DatabaseCall(self, value, callBy, q2, q3, q4, q5, q6)
