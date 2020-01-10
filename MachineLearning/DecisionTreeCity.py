"""
Questa classe si occupa di creare l'labero decisionale sulle caratteristiche di un'auto per lunghi viaggi.
"""

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class DecisionML:

    def Decison(self, q1, q2, q3, q4, q5):
        print(F"Choices: {q1} - {q2} - {q3} - {q4} - {q5}")
        DELETE = -1
        Lunghezza = 160
        ConsumoCitta = 24
        carsData = pd.read_csv("Dataset/cars.csv")
        # print(carsData.info())
        # print(carsData.head())

        # Eliminaimo le colonne non utli dal dataset
        carsData = carsData.drop('prezzo', axis=1)
        carsData = carsData.drop('cilindri', axis=1)
        carsData = carsData.drop('altezza', axis=1)
        carsData = carsData.drop('mpgautostrada', axis=1)
        carsData = carsData.drop('peso', axis=1)
        carsData = carsData.drop('symboling', axis=1)



        # Eliminiamo le vetture sopra la media per caratteristiche rilevanti e la ricalcoliamo
        print(F"Esempi di partenza (!Wne): {carsData.shape}")

        #print(mediaCitta)
        carsData = carsData.drop(carsData[(carsData.mpgcitta < ConsumoCitta)].index)
        if q3 == True: #nonUtilitaria
            carsData = carsData.drop(carsData[(carsData.lunghezza < Lunghezza)].index)
        else:
            carsData = carsData.drop(carsData[(carsData.lunghezza > Lunghezza)].index)



        mediaCitta = carsData['mpgcitta'].mean()
        mediaLunghezza = carsData['lunghezza'].mean()
        mediaLarghezza = carsData['larghezza'].mean()
        mediaCilindrata = carsData['cilindrata'].mean()
        mediaCavalli = carsData['cavalli'].mean()

        print(mediaCitta)

        data_tree = carsData

        # Setto i paramentri impostati nell Gui ed effettuo Why not encoding dove necessario
        if q2 == "Three":
            porte = 2
        else:
            porte = 4

        if q3 == True:
            AspirazioneMotore = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["aspirazione"])  # Why not encoding
        else:
            AspirazioneMotore = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["aspirazione"])

        if q4 == "ANT":
            trazione = [0, 1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q4 == "POST":
            trazione = [0, 0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q3 == True:
            trazione = [1, 0, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        else:
            trazione = DELETE
            data_tree = data_tree.drop('trazione', axis=1)

        if q5 == "BENZ":
            carburante = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        elif q5 == "DIS":
            carburante = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        else:
            carburante = DELETE
            data_tree = data_tree.drop('carburante', axis=1)

        # Costruisci l'albero decisionale
        from sklearn.tree import DecisionTreeClassifier
        from IPython.display import Image
        from sklearn.tree import export_graphviz
        import os
        from subprocess import call

        x = data_tree.drop(['marca'], axis=1)
        y = carsData['marca']

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

        print(F"Esempi su chi abbiamo fatto train e test: {x.shape}")

        tree = DecisionTreeClassifier(criterion="gini", max_depth=7)
        tree.fit(x_train, y_train)
        y_pred_train = tree.predict(x_train)
        y_pred = tree.predict(x_test)

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred)

        print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))

        value_list = [porte, mediaLunghezza, mediaLarghezza, mediaCilindrata,
                      mediaCavalli, mediaCitta]
        if trazione != DELETE:
            value_list = value_list + trazione
        if carburante != DELETE:
            value_list = value_list + carburante
        value_list = value_list + AspirazioneMotore

        print(data_tree.columns.tolist())
        print(value_list)

        predizione = tree.predict([value_list])

        print(F"Predizione: {predizione[0]}")

        os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['CONDA_PREFIX'] + r"\Library\bin\graphviz"
        export_graphviz(tree, out_file="treecity.dot", feature_names=None, rounded=True, precision=2,
                        filled=True, class_names=True)
        call(['dot', '-Tpng', 'treecity.dot', '-o', 'treecity.png'])
        Image(filename='treecity.png')

        return predizione[0]
