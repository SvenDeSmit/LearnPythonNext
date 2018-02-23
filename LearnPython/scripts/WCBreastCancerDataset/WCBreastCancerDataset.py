'''
Created on 7 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import mglearn
import mglearn.datasets as mgd

from sklearn.datasets import load_breast_cancer
cancer = load_breast_cancer()

print("cancer.keys(): \n{}".format(cancer.keys()))
print("Shape of cancer data: {}".format(cancer.data.shape))

print()
print("Target names: {}".format(cancer.target_names))

print()
print("Feature names:\n{}".format(cancer.feature_names))


print()
print("cancer.shape: {}".format(cancer.DESCR))

print(cancer)

