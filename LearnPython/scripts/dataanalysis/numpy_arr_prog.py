'''
Created on 25 feb. 2018

@author: svsm
'''

if __name__ == '__main__':
    pass

import numpy as np

points = np.arange(-5, 5, 0.01) 
print(points)

xs, ys = np.meshgrid(points,points)
print()
print(xs)
print(xs.shape)
print()
print(ys)
print(ys.shape)

print()
z = np.sqrt(xs**2+ys**2)
print(z)

import matplotlib.pyplot as plt
plt.imshow(z); plt.colorbar()
plt.title("Image plot of $\sqrt{x^2 + y^2}$ for a grid of values")
#plt.show()

a = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]
res = [num for num in a if (num % 2 == 0)]
print(res)

xarr = np.array([1.1, 1.2, 1.3, 1.4, 1.5])
yarr = np.array([2.1, 2.2, 2.3, 2.4, 2.5])
cond = np.array([True, False, True, True, False])
print()
print(xarr)
print(yarr)
print(cond)

zip1 = zip(xarr,yarr,cond)
print(np.array(zip1))
res = [(x if z else y) for x,y,z in zip1]

res = np.where(cond,xarr,yarr)
print(res)

res = np.where(cond,xarr,99)
print(res)

arr = np.random.randn(4, 4)
print()
print(arr)

print(arr > 0)

res = np.where(arr > 0,2,-2)
print(res)

print()
arr = np.random.randn(5, 4) + 10
arr = np.arange(20).reshape(5,4)
print(arr)
print(np.mean(arr))
print(np.average(arr))
print(np.sum(arr))

print()
print(np.mean(arr,axis=1))
print(np.average(arr,axis=1))
print(np.sum(arr,axis=1))

print()
print(np.mean(arr,axis=0))
print(np.average(arr,axis=0))
print(np.sum(arr,axis=0))

arr = np.array([0, 1, 2, 3, 4, 5, 6, 7])
print()
print(arr)

arr = np.array([[0, 1, 2], [3, 4, 5], [6, 7, 8]])
print()
print(arr)
print(arr.cumsum(axis=0))
print(arr.cumsum(axis=1))
print(arr.cumsum())

print()
arr = np.random.randn(100)
print(arr)
print((arr > 0).sum())

arr = np.random.randn(6)
print()
print(arr)
arr.sort()
print(arr)

arr = np.random.randn(5, 3)
print()
print(arr)
arr.sort(0)
print(arr)

arr = np.random.randn(5, 3)
print()
print(arr)
arr.sort(1)
print(arr)

arr = np.random.randn(5, 3)
print()
print(arr)
arr.sort()
print(arr)

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
print()
print(names)
print(np.unique(names))

values = np.array([6, 0, 0, 3, 2, 5, 6])
print()
print(values)
print(np.in1d(values, [2, 3, 6]))



