'''
Created on 10 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

import matplotlib as mpl

print(mpl.rcParams['axes.prop_cycle'])
evens = [2,4,6,8,10]

evens = range(2,102,2)

print(evens)
print(type(evens))

import numpy as np
npar = np.array(evens)

print(npar) 
print(type(npar))

import pandas as pd

evens2 = list(range(2,102,2))
pdds = pd.DataFrame(evens2)

print(pdds) 
print(type(pdds))

# pdds.to_csv("evens.txt", sep="\t", encoding='utf-8')

npevensfromfile = np.loadtxt('evens.txt',delimiter='\t',usecols=1,dtype=np.int32)
print()
print(npevensfromfile)

pdevensfromfile = pd.read_csv('evens.txt',sep='\t',usecols=[1])
print()
print(pdevensfromfile)

evens = list(range(2,102,2))

import matplotlib.pyplot as plt
#plt.plot(evens)

npar = np.array(evens)

plt.plot(npar,npar**2,label="x^2")
plt.legend()

plt.savefig('myplot.png',dpi=200)

plt.show()













