'''

a slightly quicker way to enter loose data into pandas


'''

__author__ = 'darren lefcoe'

# %%

import io
import pandas as pd


x = '''
    S  HZ  Z  Demand
0   0   0  0       0
1   0   0  1       0
2   0   1  0       0
3   0   1  1       0
4   0   2  0       0
5   0   2  1       0
6   1   0  0       0
7   1   0  1       0
8   1   1  0       0
9   1   1  1       0
10  1   2  0       0
11  1   2  1       0
'''

def __example():
    ''' example usage '''
    df = clean_dataframe(x)
    print(df)
    
    return


def clean_dataframe(x:str):
    ''' given a block string, returns a clean dataframe '''

    data = io.StringIO(x)
    df = pd.read_csv(data, sep='\s\s+', engine='python')
    
    return df


# main guard idiom
if __name__=='__main__':
    __example()
