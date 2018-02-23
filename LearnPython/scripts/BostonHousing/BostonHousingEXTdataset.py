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

from mglearn.datasets import load_extended_boston

X, y = mglearn.datasets.load_extended_boston()
print("X.shape: {}".format(X.shape))
print()
#print("Target names: {}".format(boston.target_names))

print(X)