'''
Created on 18 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

def f_float(val):
    try:
        return float(val)
    except ValueError:
        return val
    except TypeError:
        return  'dedju'

print(f_float(50))
print(f_float('mis'))
print(f_float((12,45)))

'''
f = open(path, 'w')
try:
    write_to_file(f)
except:
    print('Failed')
else:
    print('Succeeded')
finally:
    f.close()
    
'''    