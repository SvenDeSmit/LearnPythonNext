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

# Prepare a curve of square numbers
x = np.linspace(0,200,100) # Prepare 100 evenly spaced numbers from 
# 0 to 200
y = x**2                   # Prepare an array of y equals to x squared

# Plot a curve of square numbers
'''
'solid' or '-': Simple solid line (default)
'dashed' or '--': Dash strokes with equal spacing
'dashdot' or '-.': Alternate dashes and dots
'None', ' ', or '': No lines
'''
plt.plot(x,y,label = '$x^2$',c='burlywood',ls=('dashed'),lw=1)

plt.legend()
plt.show()

# Prepare 6 lines
x = np.linspace(0,200,100) 
y1 = x*0.5
y2 = x
y3 = x*2
y4 = x*3
y5 = x*4
y6 = x*5

# Plot lines with different dash cap styles
plt.plot(x,y1,label = '0.5x', lw=5, ls=':',dash_capstyle='butt')
plt.plot(x,y2,label = 'x', lw=5, ls='--',dash_capstyle='butt')
plt.plot(x,y3,label = '2x', lw=5, ls=':',dash_capstyle='projecting')
plt.plot(x,y4,label = '3x', lw=5, ls='--',dash_capstyle='projecting')
plt.plot(x,y5,label = '4x', lw=5, ls=':',dash_capstyle='round')
plt.plot(x,y6,label = '5x', lw=5, ls='--',dash_capstyle='round')

plt.legend()
plt.show()

# Prepare 4 lines
x = np.linspace(0,200,100)
y1 = x*2
y2 = x*3
y3 = x*4
y4 = x*5

# Set the linewidth to 2 for all lines
mpl.rcParams['lines.linewidth'] = 2

# Plot lines with different line styles
# evenly spaced 1pt dots separated by 1pt space
plt.plot(x,y1,label = '2x', ls=(0,(1,1)))
# 5pt dash followed by two 1pt dots, each separated by 3pt space
plt.plot(x,y2,label = '3x', ls=(0,(5,3,1,3,1,3)))
# 5pt dashes evenly separated by 3pt space, offset by 3
plt.plot(x,y3,label = '4x', ls=(3,(5,5)))
# 5pt dash followed by 1pt dot, offset by 2
plt.plot(x,y4,label = '5x', ls=(2,(5,2,1,2)))

plt.legend()
plt.show()

