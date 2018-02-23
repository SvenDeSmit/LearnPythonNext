'''
Created on 11 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

def append_element(some_list,element):
    some_list.append(element)

data = [1,2,3]
print(data)

append_element(data,4)
print(data)

a = 4.5 
b = 2

print('a is {0}, b is {1}'.format(type(a),type(b)))

c = a + b
print(c)
print(type(c))

d = 5
e = 2

f = d/e
print(f)
print(type(f))
print(isinstance(f,float))

def isiterable(obj):
    try:
        iter(obj)
        return True
    except TypeError: # not iterable
        return False
    
print(isiterable(5))
print(isiterable(data))
print(isiterable('ksdqhdqkdh'))

import os
print(os.getcwd())

import math
print(math.pi)

from math import pi, cos, sin
print(sin(pi))

import math as m
from math import pi as p, sin as s
print(s(p))

a = [1,2,3]
b = a
c = list(a)

print(a is b)
print(a is not c)

print(a == c)

a = None
print(a is None)


ival = 789456136
print(ival**9)

fval1 = 456.56
fval2 = 6.4e-5

print(5/2)
print(5//2) # 2

str1 = 'llsqkdqm'
str2 = "kdlqskqsmkmd"
str3 = """
skljkqlkmld
sqqdsqqd
qsdsdsd
"""
print(str3.count('\n'))

# str1[4] = 'r'

a = "this is a string"
b = a.replace('string','a longer string')
print(a)
print(b)

a = 5.6
b = str(a)
print(type(b))

a = "this is a string"
print(a[:4])
print(a[5:9])
print(a[10:])

s = '12\\45\\89'
print(s)

q = r'12\45\89'
print(q)

print(str1+str2)


template = '{0:.2f} {1:s} are worth US${2:d}'
print(template.format(45.4569,'my string',458))

val = 'espa\xc3\xb1ol'
#.encode('utf_8')
print(val)
print(val.encode('utf-8'))

s = '3.14159'
v = float(s)
print(v)
print(type(v))
i = int(v)
print(i)
print(type(i))
print(bool(i))
print(bool(0))

a = None
print(a is None)
a = 0
print(a is None)

import datetime as dt
time = dt.datetime(2017,10,29,20,56,23)
print(time)
print(time.hour)
print(time.date())
print(time.time())
print(time.strftime('%d/%m/%Y %H:%M'))

time2 = dt.datetime.strptime('20091031', '%Y%m%d')
print(time2)

time3 = time.replace(minute=0,second=0)
print(time)
print(time3)

time4 = time3 - time2
print(time2)
print(time3)
print(time4)

def myMethod(x):
    if x < 0:
        print('It\'s negative')
    elif x == 0:
        print('Equal to zero')
    elif 0 < x < 5:
        print('Positive but smaller than 5')
    else:
        print('Positive and larger than or equal to 5')

myMethod(-5)
myMethod(5)
myMethod(0)

a = 5; b = 7
c = 8; d = 4

if a > b or c < d:
    print('OK')
    
print(a < b < c)

total = 0
sequence = [1, 2, None, 4, None, 5]
for val in sequence:
    if(val is not None):
        total += val
        print(val)

print(total)


ar = [[1,2,3],[11,12,13],[21,22,23]]
print(ar)

for v1, v2, v3 in ar:
    print('{0} % {1} %{2} %'.format(v1,v2,v3))
    
x = 1
if x < 0:
    print('negative!')
elif x == 0:
    # TODO: put something smart here
    pass
else:
    print('positive!')


r1 = range(10)
print(r1)
print(type(r1))
l1 = list(r1)
print(l1)
print(type(l1))

print(list(range(0,20,2)))
print(list(range(5,-5,-1)))

a = [1,2,3,4,5]
for i in range(len(a)):
    print(a[i])

a = 15
res = 'small' if a < 10 else 'big'
print(res)










 



