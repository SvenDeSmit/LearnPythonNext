'''
Created on 4 feb. 2018

@author: Sven
'''

from sklearn.datasets.base import load_iris
from sklearn.model_selection._split import train_test_split
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
#from IPython.display import display
from pandas.plotting import scatter_matrix

if __name__ == '__main__':
    pass

# returns Bunch object
iris_ds = load_iris()


print("Keys: \n{}".format(iris_ds.keys()))

print()
print(iris_ds['DESCR'][:700] + "\n ...")

print()
print("Target names: {}".format(iris_ds['target_names']))
print("Feaure names: {}".format(iris_ds['feature_names']))

print()
print("Type of data: {}".format(type(iris_ds['data'])))
print("DS shape: {}".format(iris_ds['data'].shape))

print()
print("First 5 samples:\n {}".format(iris_ds['data'][:5]))

print()
print("Type of target: {}".format(type(iris_ds['target'])))
print("Target shape: {}".format(iris_ds['target'].shape))

print()
print("First 5 samples:\n {}".format(iris_ds['target'][:5]))

# random_state = seed => result is deterministic (always the same result fot the same seed)
Xtrain, Xtest, ytrain, ytest = train_test_split(
    iris_ds['data'],iris_ds['target'],random_state=0)
print()
print("X train => shape:\n {}".format(Xtrain.shape))
print("X train => first 5 samples:\n {}".format(Xtrain[:5]))

print()
print("X test => shape:\n {}".format(Xtest.shape))
print("X test => first 5 samples:\n {}".format(Xtest[:5]))

print()
print("y train => shape:\n {}".format(ytrain.shape))
print("y train => first 5 samples:\n {}".format(ytrain[:5]))

print()
print("y test => shape:\n {}".format(ytest.shape))
print("y test => first 5 samples:\n {}".format(ytest[:5]))


iris_df = pd.DataFrame(Xtrain,columns=iris_ds.feature_names)
print()
print(iris_df)
scatter_matrix(iris_df,
               c=ytrain,
               figsize=(10,10),
               marker='o',
               hist_kwds={'bins':20}, 
               s=20, 
               alpha=.6,
               cmap=mglearn.cm3)


from sklearn.neighbors import KNeighborsClassifier
knn = KNeighborsClassifier(n_neighbors=1)
knn.fit(Xtrain,ytrain)
print()
print(knn)

Xnew = np.array([[5,2.9,1,0.2]])
print()
print("new sample : \n{}".format(Xnew))

pred = knn.predict(Xnew)

print("Prediction: {}".format(pred))
print("Predicted target name: {}".format(
       iris_ds['target_names'][pred]))

test_pred = knn.predict(Xtest)
print()
print("Test set predictions:\n {}".format(test_pred))

res = np.mean(test_pred == ytest)
print()
print(res)

score = knn.score(Xtest,ytest)
print()
print(score)





 


print()
#print("The dataset:\n {}".format(iris_ds['data']))


print()
#print(iris_ds)

plt.show()

