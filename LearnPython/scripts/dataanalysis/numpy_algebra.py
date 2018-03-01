'''
Created on 25 feb. 2018

@author: svsm
'''

if __name__ == '__main__':
    pass
import numpy as np

x = np.array([[1., 2., 3.], [4., 5., 6.]])
y = np.array([[6., 23.], [-1, 7], [8, 9]])
print(x)
print('===')
print(y) 
print('===')

res = np.dot(x,y)
print(res)

res = x @ y
print('===')
print(res)

z = np.ones(3)
print(z)

res = np.dot(x,z) 
print('===')
print(res)

from numpy.linalg import inv, qr
print('===')
x = np.array([[1., 2., 3.], [4., 5., 6.], [7., 8., 9.]])
print(inv(x))

q, r = qr(x)
print(x)
print('===')
print()
print(q)
print(r)