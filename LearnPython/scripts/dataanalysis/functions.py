'''
Created on 17 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass
def my_func(x,y,z=1.5):
        if(z>1):
            return z*(x+y)
        else:
            return z / (x+y)
        
print(my_func(3,4))
print(my_func(3,4,1))
print(my_func(3,4,2))

print(my_func(z=2,x=3,y=4))

a = []
def func():
    a = []
    for i in range(5):
        a.append(i)
    print(a)
    
func()
print(a)

def func2():
    for i in range(5):
        a.append(i)
    print(a)

func2()
print(a)

def func3():
    global z
    for i in range(10):
        z.append(i)
    print(z)
    
#print(z)

def func4():
    a = 2
    b = 3
    c = 4
    return a,b,c 

x,y,z = func4()
print(x)
print(y)
print(z)

res = func4()
print(res)

def func5():
    a = 2
    b = 3
    c = 4
    return {'a':a,'b':b,'c':c} 

print(func5())

states = ['   Alabama ', 'Georgia!', 'Georgia', 'georgia', 'FlOrIda', 'south   carolina##', 'West virginia?']
print(states)

import re

def clean_strings(strings):
    result = []
    for value in strings:
        value = value.strip()
        value = re.sub('[!#?]', '', value)
        value = value.title()
        result.append(value)
    return result

res = clean_strings(states)
print(res)

def remove_punctuation(value):
    return re.sub('[!#?]', '', value)

print()
a = 'abc!!defg'
print(a)
b = remove_punctuation(a)
print(b)

cleanops = [str.strip, remove_punctuation, str.title]

def clean_string2(strings,ops):
    res = []
    for v in strings:
        for f in ops:
            v = f(v)
        res.append(v);
    return res

res2 = clean_string2(states,cleanops)
print(res2)

print()
for x in map(remove_punctuation,states):
    print(x)

# LAMBDA
def do_to_list(l,f):
    return [f(x) for x in l]

l1 = [1,2,3,4,5]
print(do_to_list(l1,lambda x: x * 2))
print(do_to_list(l1,lambda x: x * x))


val = 'aaac'
print(len(set(list(val)))) 

states.sort(key = lambda val: len(set(list(val))))
print(states)

# CURRYING
def f_add(a,b):
    return a + b

add_five = lambda x: f_add(5,x)
print(do_to_list(l1, add_five))

from functools import partial
add_five2 = partial(f_add,5)
print(do_to_list(l1, add_five2))

print(do_to_list(l1, partial(f_add,5)))

# ITERATORS
some_dict = {'a': 1, 'b': 2, 'c': 3}
print(type(some_dict))

for k in some_dict:
    print(k)
    
some_it = iter(some_dict)
print(type(some_it))

for k in some_it:
    print(k)

# GENERATOR
def squares(n=10):
    print('Generating squares from 1 to {0}'.format(n ** 2))
    for i in range(1, n + 1):
        yield i ** 2
        
gen = squares(20)
for x in gen:
    print(x, end=' ')

print()


print(list((x ** 2 for x in range(101))),end=' ')
print()

import itertools as it

names = ['Alan', 'Adam', 'Wes', 'Will', 'Albert', 'Steven']
for letter, nam in it.groupby(names, lambda x: x[0]):
    print('{0} : {1}'.format(letter,list(nam)))

