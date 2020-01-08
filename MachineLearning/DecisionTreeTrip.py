"""
Questa classe si occupa di creare l'labero decisionale sulle caratteristiche di un'auto per la città.
"""
from abc import abstractproperty

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class DecisionML:

    def Decison(self, q1, q2, q3, q4, q5):
        print(F"Choices: {q1} - {q2} - {q3} - {q4} - {q5}")
        DELETE = -1
        NOTDELETE = 9
        carsData = pd.read_csv("Dataset/cars.csv")
        # print(carsData.info())
        # print(carsData.head())

        # Eliminaimo le colonne non utli dal dataset
        carsData = carsData.drop('prezzo', axis=1)
        carsData = carsData.drop('cilindri', axis=1)
        carsData = carsData.drop('altezza', axis=1)
        carsData = carsData.drop('mpgcitta', axis=1)
        carsData = carsData.drop('symboling', axis=1)
        carsData = carsData.drop('aspirazione', axis=1)

        mediaAutostrada = carsData['mpgautostrada'].mean()
        mediaLunghezza = carsData['lunghezza'].mean()
        mediaLarghezza = carsData['larghezza'].mean()
        mediaCilindrata = carsData['cilindrata'].mean()
        mediaCavalli = carsData['cavalli'].mean()
        mediaPeso = carsData['peso'].mean()

        # Eliminiamo le vetture sopra la media per caratteristiche rilevanti e la ricalcoliamo
        print(F"Esempi di partenza (!Wne): {carsData.shape}")

        carsData = carsData.drop(
            carsData[(carsData.mpgautostrada > mediaAutostrada) & (carsData.cavalli < mediaCavalli)
                     & (carsData.cilindrata < mediaCilindrata)].index)
        mediaAutostrada = carsData['mpgautostrada'].mean()
        mediaCavalli = carsData['cavalli'].mean()
        mediaCilindrata = carsData['cilindrata'].mean()

        # Setto i paramentri impostati nell Gui ed effettuo Why not encoding dove necessario
        if q2 == "Three":
            porte = 2
        else:
            porte = 4

        if q3 == True:
            # LAR: 65.96565656565656 Lung: 174.37272727272722
            # print(F"LAR: {mediaLarghezza} Lung: {mediaLunghezza}")
            # Lunghezza = 190
            # Larghezza = 80
            family = NOTDELETE
            carsData = carsData.drop(
                carsData[(carsData.lunghezza < mediaLunghezza) & (carsData.larghezza < mediaLarghezza)].index)
            mediaLunghezza = carsData['lunghezza'].mean()
            mediaLarghezza = carsData['larghezza'].mean()

        else:
            family = DELETE
            carsData = carsData.drop(columns=['larghezza', 'lunghezza'], axis=1)

        '''
        Per lavorare su dataset della stessa dimensione x e y dobbiamo associre carsData a data_tree sopo 
        l'ultima possibile drop (modifica) al dataset originale
        '''

        data_tree = carsData

        if q4 == "ANT":
            trazione = [0, 1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q4 == "POST":
            trazione = [0, 0, 1]
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

        tree = DecisionTreeClassifier(criterion="gini", max_depth=6)
        tree.fit(x_train, y_train)
        y_pred_train = tree.predict(x_train)
        y_pred = tree.predict(x_test)

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred)

        '''
        Overfitting
        '''
        print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))

        value_list = [porte]
        if family == NOTDELETE:
            value_list = value_list + [mediaLunghezza, mediaLarghezza]

        value_list = value_list + [mediaPeso, mediaCilindrata,
                                   mediaCavalli, mediaAutostrada]

        if trazione != DELETE:
            value_list = value_list + trazione
        if carburante != DELETE:
            value_list = value_list + carburante

        print(data_tree.columns.tolist())
        print(value_list)

        predizione = tree.predict([value_list])

        print(F"Predizione: {predizione[0]}")

        os.environ['PATH'] = os.environ['PATH'] + ';' + os.environ['CONDA_PREFIX'] + r"\Library\bin\graphviz"
        export_graphviz(tree, out_file="treetrip.dot", feature_names=None, rounded=True, precision=2,
                        filled=True, class_names=True)
        call(['dot', '-Tpng', 'treetrip.dot', '-o', 'treetrip.png'])
        Image(filename='treetrip.png')

        return predizione[0]
