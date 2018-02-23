'''
Created on 18 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

path = 'evens.txt'

try:
    file = open(path)
    for line in file:
        print(line.rstrip())
finally:
    file.close()    

lines = [line.rstrip() for line in open(path)]
print(lines)

# auto-close file
with open(path) as file:
    lines = [line.rstrip() for line in file]
    
with open('newfile.txt','w') as file:
    for i in range(101):
        file.write('Dit is regel {0}\n'.format(i))
        
        
with open('newfile.txt') as file:
    print(file.read(10 ))
    print(file.tell())
    file.seek(3)
    print(file.read(10))
    
with open('newfile.txt','rb') as file:
    print(file.read(10))
    print(file.tell())
    




import sys    
print()
print(sys.getdefaultencoding())