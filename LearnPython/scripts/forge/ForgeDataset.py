'''
Created on 7 feb. 2018

@author: Sven
'''

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
import mglearn.datasets as mgd
#from IPython.display import display

if __name__ == '__main__':
    pass

# generate dataset
X, y = mgd.make_forge()
print(X)
print(y)


print("X.shape: {}".format(X.shape))

# plot dataset
mglearn.discrete_scatter(X[:, 0], X[:, 1], y)

plt.legend(["Class 0", "Class 1"], loc=4)
plt.xlabel("First feature")
plt.ylabel("Second feature")

# KNN

from sklearn.model_selection import train_test_split
#X, y = mglearn.datasets.make_forge()
X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=0)

from sklearn.neighbors import KNeighborsClassifier
clf = KNeighborsClassifier(n_neighbors=3)

print("X train.shape: {}".format(X_train.shape))
print("y train.shape: {}".format(y_train.shape))


clf.fit(X_train,y_train)

print("Test set predictions: {}".format(clf.predict(X_test)))
print("Test set accuracy: {:.2f}".format(clf.score(X_test, y_test)))

'''
print()
print(X_train)
print()
print(y_train)
print()
print(X_test)
print()
print(y_test)
'''

# ANALYZING

fig, axes = plt.subplots(1, 3, figsize=(10, 3))
print()
print(fig)
print()
print(axes)



for n_neighbors, ax in zip([1, 3, 9], axes):
    # the fit method returns the object self, so we can instantiate
    # and fit in one line
    clf = KNeighborsClassifier(n_neighbors=n_neighbors).fit(X, y)
    print()
    print(clf)
    
    mglearn.plots.plot_2d_separator(clf, X, fill=True, eps=0.5, ax=ax, alpha=.4)
    
    mglearn.discrete_scatter(X[:, 0], X[:, 1], y, ax=ax)
    ax.set_title("{} neighbor(s)".format(n_neighbors))
    ax.set_xlabel("feature 0")
    ax.set_ylabel("feature 1")
    axes[0].legend(loc=3)




plt.show()