'''
Created on 25 feb. 2018

@author: svsm
'''

if __name__ == '__main__':
    pass
import numpy as np

arr = np.arange(10)
print(np.sqrt(arr))
print(np.exp(arr))

x = np.random.randn(8)
y = np.random.randn(8)
print(x)
print(y)
print(np.maximum(x,y))

print()
z = np.random.randn(8) * 10
print(z)

part, whole = np.modf(z)
print(whole)
print(part)

