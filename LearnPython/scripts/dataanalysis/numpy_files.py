'''
Created on 25 feb. 2018

@author: svsm
'''

if __name__ == '__main__':
    pass

import numpy as np


names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
values = np.array([6, 0, 0, 3, 2, 5, 6])

np.save('npfile',values)

saved = np.load('npfile.npy')
print()
print(saved)

np.savez('arch_file',vals=values,strs=names)

arch = np.load('arch_file.npz')
print(arch['strs'])
print(arch['vals'])

np.savez_compressed('arch_comp',vals=values,strs=names)