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


from matplotlib.font_manager import findSystemFonts
print(findSystemFonts(fontpaths=None, fontext='ttf'))

mpl.rcParams['font.size'] = 18
mpl.rc('font', family='sans-serif')

mpl.rcParams.update({'font.size':18,'font.family':'serif' })

fontparams = {'size':16,'fontweight':'light',
              'family':'monospace','style':'normal'}

x = [1,2,3]
y = [2,4,6]
plt.plot(x,y)
plt.xlabel('xlabel',size=20,fontweight='semibold',family='sans-serif',style='italic')
plt.ylabel('ylabel',fontparams)
plt.show()

# Prepare a curve of square numbers
x = np.linspace(0,200,101) # Prepare 100 evenly spaced numbers from
# 0 to 200
y1 = x # Prepare an array of y equals to x squared
y2 = x+20 

# Plot a curve of square numbers
plt.plot(x,y1,label = '$x$')
plt.plot(x,y2,label = r'$x^2+\alpha$')

plt.legend()
plt.show()

