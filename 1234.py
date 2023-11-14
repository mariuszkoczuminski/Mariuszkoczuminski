import numpy as np
import matplotlib.pylab as plt
from sklearn import datasets
from sklearn.model_selection import train_test_split
from mlxtend.plotting import plot_decision_regions

class LogisticRegressionGD(object):

    def __init__(self, eta=0.05, n_iter=100, random_state=1):
        self.eta = eta
        self.n_iter = n_iter
        self.random_state = random_state

    def fit(self, X, y):
        rgen = np.random.RandomState(self.random_state)
        self.w_ = rgen.normal(loc=0.0, scale=0.01, size=1 + X.shape[1])
        self.cost_ = []

        for i in range(self.n_iter):
            net_input = self.net_input(X)
            output = self.activation(net_input)
            errors = (y - output)
            self.w_[1:] += self.eta * X.T.dot(errors)
            self.w_[0] += self.eta * errors.sum()
            cost = (-y.dot(np.log(output)) - ((1 - y).dot(np.log(1 - output))))
            self.cost_.append(cost)

        return self

    def net_input(self, X):
        return np.dot(X, self.w_[1:]) + self.w_[0]

    def activation(self, z):
        return 1. / (1. + np.exp(-np.clip(z, -250, 250)))

    def predict(self, X):
        return np.where(self.net_input(X) >= 0.0, 1, 0)

    def predict_proba(self, X):
        return self.activation(self.net_input(X))

def main():

    iris = datasets.load_iris()
    X = iris.data[:, [2, 3]]
    y = iris.target

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=1, stratify=y)

    # tworzenie trzech klasyfikatorów binarnych dla każdej z klas
    lrgd_0 = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)
    lrgd_1 = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)
    lrgd_2 = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)

    # uczenie modeli na podzbiorach danych z odpowiednimi wartościami docelowymi
    lrgd_0.fit(X_train[y_train == 0], np.ones(len(y_train[y_train == 0])))
    lrgd_1.fit(X_train[y_train == 1], np.ones(len(y_train[y_train == 1])))
    lrgd_2.fit(X_train[y_train == 2], np.ones(len(y_train[y_train == 2])))

    # obliczanie prawdopodobieństw przynależności do każdej z klas dla danych testowych
    proba_0 = lrgd_0.predict_proba(X_test)
    proba_1 = lrgd_1.predict_proba(X_test)
    proba_2 = lrgd_2.predict_proba(X_test)

    # wybieranie klasy z najwyższym prawdopodobieństwem jako wynik klasyfikacji wielo-klasowej
    y_pred = np.argmax(np.vstack((proba_0, proba_1, proba_2)), axis=0)

    # obliczanie dokładności klasyfikacji
    accuracy = np.sum(y_pred == y_test) / len(y_test)
    print('Accuracy: %.2f' % accuracy)

  #w regresji logarytmicznej wyjście przyjmuje wartości 0 lub 1 (prawdopodobieństwa)
    X_train_01_subset = X_train[(y_train == 0) | (y_train == 1)]
    y_train_01_subset = y_train[(y_train == 0) | (y_train == 1)]
    lrgd = LogisticRegressionGD(eta=0.05, n_iter=1000, random_state=1)
    lrgd.fit(X_train_01_subset, y_train_01_subset)
    plot_decision_regions(X=X_train_01_subset, y=y_train_01_subset, clf=lrgd)
    plt.xlabel(r'$x_1$')
    plt.ylabel(r'$x_2$')
    plt.legend(loc='upper left')
    plt.show()

if __name__ == '__main__':
    main()
