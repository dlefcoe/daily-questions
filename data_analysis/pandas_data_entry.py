'''

a slightly quicker way to enter loose data into pandas


'''

# %%

import io
import pandas as pd


x = '''
Index    Value    Max(3)    Min(3)    State
0    10    nan    nan    nan
1    20    nan    nan    nan    
2    15    nan    nan    nan     
3    25    20     10     1
4    15    25     15     2
5    10    25     15     4
6    15    20     10     3    
'''


data = io.StringIO(x)


df = pd.read_csv(data, sep='    ')
df

