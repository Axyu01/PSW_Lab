import numpy as np
import matplotlib.pyplot as plt
import skimage as img
from skimage import data
from scipy import ndimage
from sklearn.datasets import load_digits
from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import RepeatedStratifiedKFold
from sklearn.metrics import balanced_accuracy_score
import random

X,y = load_digits(return_X_y=True)
print(X)
print(y)

mean_results = []
for j in range(5):
    rskf = RepeatedStratifiedKFold(n_splits=2,n_repeats=5)

    mean_result = []
    for i, (train_index, test_index) in enumerate(rskf.split(X, y)):
        X_train,y_train = [],[]
        X_test,y_test = [],[]
        for x,index in enumerate(train_index):
            X_train.append(X[index])
            y_train.append(y[index])
        for x,index in enumerate(test_index):
            X_test.append(X[index])
            y_test.append(y[index])
        hidden_layer_sizes = np.ones((j+1)).astype(int)*10
        classifier = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes,max_iter=100)
        classifier.fit(X_train,y_train)
        y_out = classifier.predict(X_test)
        #print("Prob",j,i,y_out)
        mean_result.append(balanced_accuracy_score(y_test,y_out))
    mean_results.append(np.mean(np.array(mean_result)))

print(mean_results)
print("Best:",np.argmax(mean_results))

