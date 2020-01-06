import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import log_loss
from sklearn.metrics import accuracy_score

"""
se passo una lista in base alla domanda degli attributi da non deover 
tenere conto riesco a sfoltire l'albero man mano. Poi dopo un certo numero di domando diamo una riusposta
"""


class MLStep1:

    def __init__(self):
        carsData = pd.read_csv("Dataset/cars.csv")

        print(carsData.info())
        print(carsData.head())

        carsData["prezzo"] = carsData["prezzo"].astype('int64')
        carsData["cavalli"] = carsData["cavalli"].astype('int64')
        carsData = pd.get_dummies(carsData)
        print(carsData.info())
        print(carsData.head())

        x = carsData.drop("prezzo", axis=1).values
        y = carsData['prezzo'].values

        x_train, x_test, y_train, y_test = train_test_split(x, y, test_size=0.3, random_state=0)

        from sklearn.tree import DecisionTreeClassifier
        tree = DecisionTreeClassifier(criterion="gini")
        tree.fit(x_train, y_train)
        y_pred_train = tree.predict(x_train)
        y_pred = tree.predict(x_test)

        accuracy_train = accuracy_score(y_train, y_pred_train)
        accuracy_test = accuracy_score(y_test, y_pred)

        print("ACCURACY: TRAIN=%.4f TEST=%.4f" % (accuracy_train, accuracy_test))

        '''
        from sklearn.tree import export_graphviz
        import pydotplus

        from subprocess import call
        from IPython.display import Image

        export_graphviz(tree, out_file='tree.dot')

        # Convert to png using system command (requires Graphviz)
        from subprocess import call
        call(["dot", "-Tpng", "tree.dot", "-o", "tree.png", "-Gdpi=600"])

        from IPython.display import Image
        Image(filename='tree.png')
        '''
