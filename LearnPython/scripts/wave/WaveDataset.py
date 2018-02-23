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

X, y = mgd.make_wave(n_samples=40)
print(X)
print(y)


plt.plot(X, y, 'o')
plt.ylim(-3, 3)
plt.xlabel("Feature")
plt.ylabel("Target")

plt.show()