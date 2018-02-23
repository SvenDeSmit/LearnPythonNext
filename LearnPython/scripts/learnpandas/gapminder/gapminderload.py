'''
Created on 10 feb. 2018

@author: Sven
'''

if __name__ == '__main__':
    pass

import pandas as pd

import os
print(os.getcwd())

df = pd.read_csv('gapminder.tsv', sep='\t')
# we use the head method so Python shows us only the first 5 rows

print(type(df))


print(df.head())