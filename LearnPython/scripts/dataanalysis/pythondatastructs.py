'''
Created on 11 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

tup = 4,5,6
print(tup)
print(type(tup))

tupoftup = (4,5,6),(14,15,16)
print(tupoftup)
print(type(tupoftup))

a = [1,2,3,4,5]
atup = tuple(a)
print()
print(atup)
print(type(atup))

al = list(a)
print()
print(al)
altup = tuple(al)
print()
print(altup)
print(type(altup))

strtup = tuple('my string')
print()
print(strtup)
print(type(strtup))

print(strtup[5])

tup = tuple(['foo', [1, 2], True])
#tup[2] =False
tup[1].append(3)
print(tup)

a = [1,2,3,4,5]
b = ['a','b']
c= a + b
print(c)

d = c*4
print(d)

a1, a2, a3, a4, a5 = a
print(a3)

tupoftup = (4,5,6),(14,15,16)
(a, b, c),(d,e,f) = tupoftup
print(e)

for a,b,c in tupoftup:
    print(a+b+c);
    
a = [1,2,3,4,5]
x,y, *rest = a
print(x)
print(rest)

x,y, *_ = a
print(x)
print(_)

t = 1,2,3,4,2,4,5,4
print(t.count(4))

print()
l1 = [1,2,3,4,5,None]
print(l1)

tup = ('a','b','c')
print(tup)
tl = list(tup)
print(tl)

gen = range(1,10)
print(gen)
lgen = list(gen)
print(lgen)

print()
tl.append('d')
print(tl)

tl.insert(2,'x')
print(tl)

x = tl.pop(2)
print(x)
print(tl)

tl.remove('c')
print(tl)

print('a' in tl)
print('a' not in tl)
    
l1 = [1,2,3,4,5]
l2 = [10,11,12,13,14,15]
l3 = l1 + l2
print()
print(l3) 

x = [4, None, 'foo']
print(x)
x.extend([7,8,[17,17]])
print(x)

numbers = []
for val in x:
    if(type(val) == int):
        numbers.append(val)
print(numbers)

a = [7,6,9,2,5,8]
print()
print(a)
a.sort()
print(a)

b = ['saw', 'small', 'He', 'foxes', 'six']
print(b)
b.sort()
print(b)

b = ['saw', 'small', 'He', 'foxes', 'six']
b.sort(key=len)
print(b)

import bisect
print()
print(a)
print(bisect.bisect(a,6))
bisect.insort(a,6)
print(a)

print(a[3:6])
a[3:5] = [9,9]
print(a) 

print(a[3:])
print(a[:3])

print(a[-4:])
print(a[-6:-2])

print(a[::2])
print(a[::3])

print(a[::-1])

print()
b = ['saw', 'small', 'He', 'foxes', 'six']
for value in b:
    print(value)
    
for i, value in enumerate(b):
    print('{0} : {1}'.format(i,value))
    
print()
for v in sorted(b):
    print(v)    

print(sorted('This is my string'))

seq1 = [1,2,3]
seq2 = [11,12,13]
zipped = zip(seq1,seq2)
print(list(zipped))

seq1 = [1,2,3]
seq2 = [11,12]
zipped = zip(seq1,seq2)
print(list(zipped))

seq1 = [1,2,3]
seq2 = [11,12,13]
for i, (a,b) in enumerate(zip(seq1,seq2)):
    c= a + b
    print('{0} : {1}'.format(i,c))
rev = list(reversed(seq1))
print(rev)

d1 = {}
d2 = {'k1':'v1','k2':'v2','k3':'v3'}
print()
print(d2)

d3 = {'k1':'v1','k2':12,'k3':[4,5,6]}
print(d3)

print()
d2['k4'] = 'v4'
print(d2)

print(d2['k2'])
print('k3' in d2)
print('k5' in d2)

print()
print(d2.keys())
print(list(d2.keys()))
print(list(d2.values()))

print()
del d2['k2']

print(d2)

p = d2.pop('k4')
print(d2)

print()
d2 = {'k1':'v1','k2':'v2','k3':'v3'}
d3 = {'k1':'v11','k3':[4,5,6]}
print(d2)
d2.update(d3)
print(d2)

print()
d2 = {'k1':'v1','k2':'v2','k3':'v3'}
l1 = list(d2.keys())
l2 = list(d2.values())
print(l1)
print(l2)
d5 = {}
for k,v in zip(l1,l2):
    d5[k] = v
print(d5)

print(d5['k2'])
print(d5.get('k2'))
print(d5.get('k2','v??'))

# print(d5['k5'])
print(d5.get('k5'))
print(d5.get('k5','v??'))

print()
s2 = {2,5,8,7,8,5,3,6,6,1,1,2}
print(s2)
s1 = set([2, 2, 2, 11, 13, 3,1])
print(s1)

s3 = s1.union(s2)
print(s3)

s3 = s1 | s2
print(s3)

s4 = s1.intersection(s2)
print(s4)
s4 = s1 & s2
print(s4)

print()
a = {1, 2, 3, 4, 5}
b = {3, 4, 5, 6, 7, 8}
c = a.copy()
c |= b
print(c)
d = a.copy()
d &= b
print(d)

ss = {3,4,5} 
print(ss.issubset(b))
print(b.issuperset(ss))

print({1,2,3} == {3,2,1})

# COMPEHENSIONS
strings = ['a', 'as', 'bat', 'car', 'dove', 'python']

print()
res = [x.upper() for x in strings]
print(res)

res = [x.upper() for x in strings if len(x) > 2]
print(res)

s = set(strings)
print(s)
res = {x.upper() for x in strings if len(x) > 2}
print(res)

keys = ['k1','k2','k3','k4','k5','k6']

ul = {len(x) for x in strings}
print(ul)

print(set(map(len,strings)))
idxmap = {val : index for index, val in enumerate(strings)}
print(idxmap)
print(idxmap['car'])

print()
all_data = [['John', 'Emily', 'Michael', 'Mary', 'Steven'],['Maria', 'Juan', 'Javier', 'Natalia', 'Pilar']]
print(all_data)

res = [name for names in all_data for name in names]
print(res)

res = [name for names in all_data for name in names if name.count('e') > 0]
print(res)

