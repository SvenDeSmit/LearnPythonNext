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
from matplotlib.lines import Line2D

# Prepare 100 random numbers to plot
x = np.random.rand(100)
y = np.random.rand(100)
# Prepare 100 random numbers within the range of the number of
# available markers as index
# Each random number will serve as the choice of marker of the
# corresponding coordinates
markerindex = np.random.randint(0, len(Line2D.markers), 100)
print(markerindex)

# shows possible markers and abbreviation
print(Line2D.markers)

# Plot all kinds of available markers at random coordinates
# for each type of marker, plot a point at the above generated
# random coordinates with the marker type
for k, m in enumerate(Line2D.markers):
    i = (markerindex == k)
    plt.scatter(x[i], y[i], marker=m)

plt.show()

# Prepare 5 lines
x = np.linspace(0,20,10)
y1 = x
y2 = x*2
y3 = x*3
y4 = x*4
y5 = x*5


# Plot lines with different marker sizes
plt.plot(x,y1,label = 'x', lw=1, marker='s', ms=5)  # square size 10
plt.plot(x,y2,label = '2x', lw=1, marker='^', ms=6) # triangle size 12
plt.plot(x,y3,label = '3x', lw=1, marker='o', ms=5) # circle size 10
plt.plot(x,y4,label = '4x', lw=1, marker='D', ms=4)  # diamond size 8
plt.plot(x,y5,label = '5x', lw=1, marker='P', ms=6) # filled plus sign
# size 12

# get current axes and store it to ax
ax = plt.gca()
plt.legend()
plt.show()
