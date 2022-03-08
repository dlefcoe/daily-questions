import pandas as pd

# read the data
df = pd.read_csv('test_csv.csv')

# build the new column
df['filter']='-'
for index, row in df.iterrows():
    if row['from'] + '-' + row['to'] not in df['filter'].values:
        if row['to'] + '-' + row['from'] not in df['filter'].values:
            df.loc[index,'filter']= row['from'] + '-' + row['to']    


print(df)
