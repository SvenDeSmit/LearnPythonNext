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

from sklearn.datasets import load_boston
boston = load_boston()

print("Data shape: {}".format(boston.data.shape))

print()
#print("Target names: {}".format(boston.target_names))

print()
print("DESCR: {}".format(boston.DESCR))

print(boston)