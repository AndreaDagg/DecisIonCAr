import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score


class DecisionML():
    def __init__(self, q1, q2, q3, q4, q5):
        DELETE = -1
        carsData = pd.read_csv("Dataset/cars.csv")
        # print(carsData.info())
        # print(q1 + " " + q2 + " " + " " + q4 + " " + q5)

        # Eliminaimo le colonne non utli dal dataset
        carsData = carsData.drop('prezzo', axis=1)
        carsData = carsData.drop('cilindri', axis=1)
        carsData = carsData.drop('altezza', axis=1)
        carsData = carsData.drop('mpgautostrada', axis=1)
        carsData = carsData.drop('peso', axis=1)
        carsData = carsData.drop('symboling', axis=1)
        # carsData = carsData.drop('marca', axis=1)

        mediaCitta = carsData['mpgcitta'].mean()
        mediaLunghezza = carsData['lunghezza'].mean()
        mediaLarghezza = carsData['larghezza'].mean()
        mediaCilindrata = carsData['cilindrata'].mean()
        mediaCavalli = carsData['cavalli'].mean()

        data_tree = carsData

        if q2 == "Three":
            porte = 2
        else:
            porte = 4

        if q3 == True:
            AspirazioneMotore = "turbo"
            AspirazioneMotore = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["aspirazione"])  # Why not encoding
        else:
            AspirazioneMotore = "std"
            AspirazioneMotore = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["aspirazione"])

        if q4 == "ANT":
            trazione = "fwd"
            trazione = [0, 1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q4 == "POST":
            trazione = "rwd"
            trazione = [0, 0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        elif q3 == True:
            trazione = "4wd"
            trazione = [1, 0, 0]
            data_tree = pd.get_dummies(data_tree, columns=["trazione"])
        else:
            trazione = DELETE
            data_tree = data_tree.drop('trazione', axis=1)

        if q5 == "BENZ":
            carburante = "gas"
            carburante = [0, 1]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        elif q5 == "DIS":
            carburante = "diesel"
            carburante = [1, 0]
            data_tree = pd.get_dummies(data_tree, columns=["carburante"])
        else:
            carburante = DELETE
            data_tree = data_tree.drop('carburante', axis=1)

        # data_tree = pd.get_dummies(data_tree)

        print(data_tree.columns.tolist())
        print(data_tree.info())
        print(data_tree.head())
        # print(carsData.columns.tolist())

        from sklearn import tree
        x = data_tree.drop(['marca'], axis=1)
        y = carsData['marca']

        '''
        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)
        print(x.shape)

       

        tree = DecisionTreeClassifier(criterion="gini")
        tree.fit(x_train, y_train)
        y_pred_train = tree.predict(x_train)
        y_pred = tree.predict(x_test)

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred)

        print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))
        '''

        tree_clf = tree.DecisionTreeClassifier(criterion='gini', max_features=None, splitter='best')
        tree_clf = tree_clf.fit(x, y)

        # Nel Peggiore dei casi
        # ['porte', 'lunghezza', 'larghezza', 'cilindrata', 'cavalli', 'mpgcitta', 'trazione_4wd', 'trazione_fwd', 'trazione_rwd', 'carburante_diesel', 'carburante_gas', 'aspirazione_std', 'aspirazione_turbo']

        '''
        print(porte)
        print(trazione)
        print(carburante)
        print(carsData.info())
        print(AspirazioneMotore)
        print(" - - - - - - - - ")
        print(data_tree.info())
        print(data_tree.columns.tolist())
        '''
        print(mediaCavalli)
        print(mediaCilindrata)
        print(mediaCitta)
        exsample = [porte, mediaLunghezza, mediaLarghezza, mediaCilindrata,
                    mediaCavalli]
        if trazione != DELETE:
            exsample = exsample + trazione
        if carburante != DELETE:
            exsample = exsample + carburante

        print(exsample)

        risultati = tree_clf.predict([exsample])
        print(risultati)
