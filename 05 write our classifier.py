# encoding: utf-8
"""
@author: suns
@contact: sunshuai0518@gmail.com
@time: 2019/6/26 3:44 PM
@file: 05 write our classifier.py
@desc:
"""

from scipy.spatial import distance
import random
from sklearn import datasets
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def euc(a, b):
    return distance.euclidean(a, b)


class ScrappyKNN():

    def fit(self, X_train, y_train):
        self.X_train = X_train
        self.y_train = y_train

    def predict(self, X_test):
        predictions = []
        for row in X_test:
            label = self.closest(row)
            predictions.append(label)
        return predictions

    # 简化版k近邻，k=1
    def closest(self, row):
        best_dist = euc(row, self.X_train[0])
        best_index = 0
        for i in range(1, len(self.y_train)):
            dist = euc(row, self.X_train[1])
            if dist < best_dist:
                best_dist = dist
                best_index = 1
        return self.y_train[best_index]


iris = datasets.load_iris()

X = iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.5)
# my_classifier = tree.DecisionTreeClassifier()
# my_classifier = KNeighborsClassifier()
my_classifier = ScrappyKNN()
my_classifier.fit(X_train, y_train)

predictions = my_classifier.predict(X_test)
print(accuracy_score(y_test, predictions))
