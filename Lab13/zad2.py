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

X_closed,y_closed = [],[]
X_open,y_open = [],[]
for i in range(len(X)):
    if(y[i]<5):
        X_closed.append(X[i])
        y_closed.append(y[i])
    else:
        X_open.append(X[i])
        y_open.append(y[i])
#

rskf = RepeatedStratifiedKFold(n_splits=2,n_repeats=5)

inner_mean_result = []
outer_mean_result = []
for i, (train_index, test_index) in enumerate(rskf.split(X_closed, y_closed)):
    X_train,y_train = [],[]
    X_test,y_test = [],[]
    for x,index in enumerate(train_index):
        X_train.append(X_closed[index])
        y_train.append(y_closed[index])
    for x,index in enumerate(test_index):
        X_test.append(X_closed[index])
        y_test.append(y_closed[index])
    hidden_layer_sizes = np.ones((5)).astype(int)*10
    classifier = MLPClassifier(hidden_layer_sizes=hidden_layer_sizes,max_iter=100)
    classifier.fit(X_train,y_train)
    y_out = classifier.predict(X_test)
    #print("Prob",j,i,y_out)
    inner_score = balanced_accuracy_score(y_test,y_out)
    inner_mean_result.append(inner_score)

    X_mixed = X_test + X_open
    y_mixed = y_test + y_open
    for j in range(len(y_mixed)):
        if(y_mixed[j]<5):
            y_mixed[j] = 1
        else:
            y_mixed[j] = 0
    probs = classifier.predict_proba(X_mixed)
    probs = np.max(probs,axis=1)

    threshold = 0.8
    y_out = probs
    y_out[y_out>=0.8] = 1
    y_out[y_out<0.8] = 0
    outer_score = balanced_accuracy_score(y_mixed,y_out)
    outer_mean_result.append(outer_score)
inner_mean = np.mean(np.array(inner_mean_result))
outer_mean = np.mean(np.array(outer_mean_result))
    
print("Inner score:",inner_mean)
print("Outer score:",outer_mean)
