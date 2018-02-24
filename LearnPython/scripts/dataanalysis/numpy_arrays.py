'''
Created on 24 feb. 2018

@author: svsm
'''

if __name__ == '__main__':
    pass

import numpy as np


#print(my_arr)
#print(my_list)

'''

my_arr = np.arange(1000000)
my_list = list(range(1000000))

import time 
start = time.time()
print(start)
for _ in range(100): my_arr2 = my_arr * 2
end = time.time()
print(end-start)

start = time.time()
print(start)
for _ in range(100): my_list2 = my_list * 2
end = time.time()
print(end-start)
'''

data = np.random.randn(2,3)
print(data)

d2 = data * 10
print(d2)

d3 = np.random.randn(2,3) * 10
print(d3)
d4 = d2 + d3
print(d4)
print(d4.dtype)

d1 = [6,7.5,8,0,1]
print(d1)
a1 = np.array(d1)
print(a1)
print(a1.dtype)

print()
d2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print(d2)
a2 = np.array(d2)
print(a2)
print(a2.ndim)
print(a2.shape)
print(a2.dtype)

a3 = np.zeros(10)
print(a3)

a3 = np.zeros((3,6))
print(a3)

a3 = np.empty((3,6,2))
print(a3)

print()
a4 = np.arange(15)
print(a4)

a5 = np.eye(5)
print(a5)

print()
a6 = np.array([1,2,3], dtype=np.float64)
print(a6)

a7 = a6.astype(np.int64)
print(a7)

print()
a8 = np.array(['1.25', '-9.6', '42'], dtype=np.string_)
print(a8)
a9 = a8.astype(np.float64)
print(a9)

a10 = np.array([.22, .270, .357, .380, .44, .50], dtype=np.float64)
print(a10)

