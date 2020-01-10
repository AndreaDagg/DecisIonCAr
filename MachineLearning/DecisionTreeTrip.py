"""
Questa classe si occupa di creare l'labero decisionale sulle caratteristiche di un'auto per la città.
"""
from abc import abstractproperty

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


class DecisionML:

    def Decison(self, q1, q2, q3, q4, q5, Prezzo):
        print(F"Choices: {q1} - {q2} - {q3} - {q4} - {q5}")
        DELETE = -1
        NOTDELETE = 9
        carsData = pd.read_csv("Dataset/cars.csv")
        # print(carsData.info())
        # print(carsData.head())

        # Eliminaimo le colonne non utli dal dataset

        carsData = carsData.drop('cilindri', axis=1)
        carsData = carsData.drop('larghezza', axis=1)
        carsData = carsData.drop('mpgcitta', axis=1)
        carsData = carsData.drop('symboling', axis=1)
        carsData = carsData.drop('aspirazione', axis=1)

        # Eliminiamo le vetture sopra la media per caratteristiche rilevanti e la ricalcoliamo
        print(F"Esempi di partenza (!Wne): {carsData.shape}")

        mediaAutostrada = carsData['mpgautostrada'].mean()
        print(F"AUT=> {mediaAutostrada}")
        carsData = carsData.drop(carsData[(carsData.mpgautostrada < 28)].index)

        # mediaCilindrata = carsData['cilindrata'].mode()
        # print(mediaCilindrata)
        minimoCilindrata = 87
        carsData = carsData.drop(carsData[(carsData.cilindrata < minimoCilindrata)].index)

        mediaAutostrada = carsData['mpgautostrada'].mean()
        mediaCavalli = carsData['cavalli'].mean()
        mediaCilindrata = carsData['cilindrata'].mean()
        mediaPeso = carsData['peso'].mean()
        mediaLunghezza = carsData['lunghezza'].mean()
        mediaAltezza = carsData['altezza'].mean()

        # Setto i paramentri impostati nell Gui ed effettuo Why not encoding dove necessario
        if q2 == "Three":
            porte = 2
            MINLUNGHEZZA = 170
            carsData = carsData.drop(carsData[(carsData.lunghezza > MINLUNGHEZZA)].index)
        else:
            porte = 4

        if q3 == True:
            family = NOTDELETE
            MINALTEZZA = 55.5
            MINLUNGHEZZA = 160
            carsData = carsData.drop(carsData[(carsData.lunghezza < MINLUNGHEZZA)].index)
            carsData = carsData.drop(carsData[(carsData.altezza < MINALTEZZA)].index)

            mediaLunghezza = carsData['lunghezza'].mean()
            mediaAltezza = carsData['altezza'].mean()

        else:
            family = DELETE
            carsData = carsData.drop(columns=['altezza', 'lunghezza'], axis=1)

        '''
        I.A. 
        Per lavorare su dataset della stessa dimensione x e y dobbiamo associre carsData a data_tree sopo 
        l'ultima possibile drop (modifica) al dataset originale. 
        Ha senso calcolare il prezzo medio solo sul dataset opportunamente calcolato. 
        '''
        if not isinstance(Prezzo, int):
            Prezzo = carsData['prezzo'].mean()
        data_tree = carsData

        if q4 == "ANT" and 'rwd' in data_tree['trazione'].values:
            print("Selezionato Ant, esiste rwd")
            trazione = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q4 == "POST" and 'fwd' in data_tree['trazione'].values:
            print("Selezionato POST, esiste fwd")
            trazione = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        else:
            print("cancello")
            trazione = DELETE
            data_tree = data_tree.drop('trazione', axis=1)

        if q5 == "BENZ" and 'diesel' in data_tree['carburante'].values:
            carburante = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        elif q5 == "DIS" and 'gas' in data_tree['carburante'].values:
            carburante = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        else:
            carburante = DELETE
            data_tree = data_tree.drop('carburante', axis=1)

        print(data_tree.columns.tolist())
        print(F"Esempi elaborati (!Wne): {data_tree.shape}")

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
            value_list = value_list + [mediaLunghezza, mediaAltezza]

        value_list = value_list + [mediaPeso, mediaCilindrata,
                                   mediaCavalli, mediaAutostrada]

        value_list = value_list + [Prezzo]

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
