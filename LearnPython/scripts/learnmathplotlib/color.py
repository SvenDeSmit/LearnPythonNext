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

years = list(range(2009,2017))
android = [6.8,67.22,220.67,451.62,761.29,1004.68,1160.21,1271.02]
ios = [24.89,46.6,89.27,130.13,150.79,191.43,225.85,216.07]
microsoft = [15.03,12.38,8.76,16.94,30.71,35.13,26.74,6.94]

plt.plot(years,android,label='Android',c='C3')     # color='C0' by default
plt.plot(years,ios,label='iOS',c='C4')             # color='C1' by default
plt.plot(years,microsoft,label='Microsoft',c='C5') # color='C2' by default

plt.legend()
plt.show()

# Prepare 4 lines with different slopes
x = np.linspace(0,200,101) # Prepare 100 evenly spaced numbers from
print()
print(x)
#  0 to 200
y1 = x*2
y2 = x*3
y3 = x*4
y4 = x*5

# Set line width to 2 for clarity
mpl.rcParams['lines.linewidth'] = 2 

# Drawing the 4 lines
plt.plot(x,y1,label = '2x', c='0')             # Black solid line 
plt.plot(x,y2,label = '3x', c='0.2', ls='--')  # Dark grey dashed line
plt.plot(x,y3,label = '4x', c='0.4', ls='-.')  # Grey dash-dot line
plt.plot(x,y4,label = '5x', c='0.6', ls=':')   # Light grey dotted line

plt.legend()
plt.show()