'''
Created on 10 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass


import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import matplotlib as mpl

# Prepare 100 evenly spaced numbers from 0 to 200
evens = np.linspace(0,200,101)

# Plot a square curve
plt.plot(evens,evens**2,label = 'x^2')

# Adding grid lines

plt.grid(color='lightblue', linestyle='-.', linewidth=0.3)

plt.legend()
plt.show()