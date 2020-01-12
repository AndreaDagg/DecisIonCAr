"""
Questa classe si occupa di creare l'labero decisionale sulle caratteristiche di un'auto berline.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class DecisionML:

    def Decison(self, q1, q2, q3, q4, q5, Prezzo):
        print(F"Choices: {q1} - {q2} - {q3} - {q4} - {q5} - Prezzo: {Prezzo}")
        DELETE = -1
        MINCILINDRI = 6
        carsData = pd.read_csv("Dataset/cars.csv")
        # print(carsData.info())
        # print(carsData.head())

        # Eliminaimo le colonne non utli dal dataset
        carsData = carsData.drop('larghezza', axis=1)
        carsData = carsData.drop('cilindri', axis=1)
        carsData = carsData.drop('peso', axis=1)
        carsData = carsData.drop('symboling', axis=1)
        carsData = carsData.drop('aspirazione', axis=1)
        carsData = carsData.drop('cavalli', axis=1)

        # Eliminiamo le vetture sopra la media per caratteristiche rilevanti e la ricalcoliamo
        print(F"Esempi di partenza (!Wne): {carsData.shape}")

        # carsData = carsData.drop(carsData[(carsData.altezza <)].index)

        mediaCitta = carsData['mpgcitta'].mean()
        carsData = carsData.drop(carsData[(carsData.mpgcitta < mediaCitta)].index)

        mediaAutostrada = carsData['mpgautostrada'].mean()
        carsData = carsData.drop(carsData[(carsData.mpgautostrada < mediaAutostrada)].index)

        mediaLunghezza = carsData['lunghezza'].mean()  # Valutare se drop
        mediaCilindrata = carsData['cilindrata'].mean()

        # Setto i paramentri impostati nell Gui ed effettuo Why not encoding dove necessario
        if q2 == "Three":
            porte = 2
            # carsData = carsData.drop(carsData[(carsData.lunghezza == 4)].index)
            carsData = carsData.drop(carsData[(carsData.cilindrata > mediaCilindrata)].index)
        else:
            porte = 4
            # carsData = carsData.drop(carsData[(carsData.lunghezza == 2)].index)
            carsData = carsData.drop(carsData[(carsData.cilindrata < mediaCilindrata)].index)

        if q3 == True:
            carsData = carsData.drop(carsData[(carsData.lunghezza < mediaLunghezza)].index)
        else:
            LungEsagerataCitta = 180
            carsData = carsData.drop(carsData[(carsData.lunghezza > LungEsagerataCitta)].index)

        if not isinstance(Prezzo, int):
            Prezzo = carsData['prezzo'].mean()
        data_tree = carsData

        if (q4 == "ANT") and ('rwd' in data_tree['trazione'].values) and ('fwd' in data_tree['trazione'].values):

            trazione = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])

        elif (q4 == "POST") and ('rwd' in data_tree['trazione'].values) and ('fwd' in data_tree['trazione'].values):

            trazione = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        else:
            trazione = DELETE
            data_tree = data_tree.drop('trazione', axis=1)

        if (q5 == "BENZ") and ('gas' in data_tree['carburante'].values) and (
                'diesel' in data_tree['carburante'].values):

            carburante = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])

        elif (q5 == "DIS") and ('gas' in data_tree['carburante'].values) and (
                'diesel' in data_tree['carburante'].values):

            carburante = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])

        else:
            carburante = DELETE
            data_tree = data_tree.drop('carburante', axis=1)

        mediaAutostrada = data_tree['mpgautostrada'].mean()
        mediaCilindrata = data_tree['cilindrata'].mean()
        mediaAltezza = data_tree['altezza'].mean()
        print(data_tree.columns.tolist())

        # Costruisci l'albero decisionale
        from sklearn.tree import DecisionTreeClassifier
        from IPython.display import Image
        from sklearn.tree import export_graphviz
        import os
        from subprocess import call
        from matplotlib import pyplot as plt

        x = data_tree.drop(['marca'], axis=1)
        y = carsData['marca']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

        print(F"Esempi su chi abbiamo fatto train e test: {x.shape}")

        tree = DecisionTreeClassifier(criterion="gini")
        tree.fit(x_train, y_train)  # Build a decision tree from the training set (X, y).
        y_pred_train = tree.predict(x_train)  # the predicted class for each sample in X is returned
        y_pred = tree.predict(x_test)

        plt.scatter(y_train, y_pred_train)
        plt.xlabel("True value")
        plt.ylabel("Prediction")
        plt.show()

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred)

        print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))

        value_list = [porte, mediaLunghezza, mediaAltezza, mediaCilindrata, mediaCitta, mediaAutostrada, Prezzo]
        # print(F"Porte {porte}, lung {mediaLunghezza} alte {mediaAltezza} cilind {mediaCilindri} cilindra {mediaCilindrata} cavall {mediaCavalli}")
        if trazione != DELETE:
            value_list = value_list + trazione
        #   print(F"traz {trazione}")
        if carburante != DELETE:
            value_list = value_list + carburante
        #  print(F"ccarb {carburante}")

        print(data_tree.columns.tolist())
        print(value_list)

        predizione = tree.predict([value_list])
        path = tree.decision_path([value_list])

        print(F"Predizione: {predizione[0]}")

        os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['CONDA_PREFIX'] + r"\Library\bin\graphviz"
        export_graphviz(tree, out_file="treerace.dot", feature_names=None, rounded=True, precision=2,
                        filled=True, class_names=True)
        call(['dot', '-Tpng', 'treerace.dot', '-o', 'treerace.png'])
        Image(filename='treerace.png')

        print(path)
        return predizione[0]
