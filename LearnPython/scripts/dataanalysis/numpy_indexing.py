'''
Created on 24 feb. 2018

@author: svsm
'''
from h5py.tests import old

if __name__ == '__main__':
    pass

import numpy as np

arr = np.arange(10)
print(arr)

print(arr[5])
print(arr[5:8])

arr[5:8] = 99
print(arr)

print()
arr = np.arange(10)
print(arr)
sl = arr[5:8]
print(sl)
sl[1] = 99
print(arr)
sl[:] = 999
print(arr)

arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print()
print(arr2d[1])
print(arr2d[1][1])
print(arr2d[1,1])

print()
arr3d = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
print(arr3d)
print(arr3d[1])
print(arr3d[1,1])
print(arr3d[1,1,1])

old = arr3d[0].copy()
print()
print(arr3d)
print(arr3d[0])
arr3d[0] = 99
print(arr3d)

arr3d[0] = old
print(arr3d)

print()
print(arr2d)
print(arr2d[:2])
print(arr2d[:2,1:])

print()
print(arr2d[0,:2])
print(arr2d[:2,2])

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = np.random.randn(7, 4)
print()
print(names)
print(data)

filter = (names == 'Joe')
print(filter)
print(data[filter])

print()
print(data[filter,2:])
print(data[filter,3])

print()
print(data[~filter])

filter = (names == 'Joe') | (names == 'Bob')
print()
print(data[filter])

print()
data[data < 0] = 0
print(data)

arr = np.empty((8,4))
print()
print(arr)
for i in range(8):
    arr[i] = i
print(arr)

print(arr[[4,2,7]])    

arr2 = np.arange(32).reshape((8,4))
print()
print(arr2)
print(arr2[[1,2,3,4],[0,1,2,3]])
print()
print(arr2[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
   
print()    
arr3 = np.arange(15).reshape((3,5))
print(arr3)
print(arr3.T)

print()
print(np.dot(arr3.T,arr3))

arr4 = np.arange(16).reshape((2, 2, 4))
print()
print(arr4)
print(arr4.transpose((1,0,2)))
