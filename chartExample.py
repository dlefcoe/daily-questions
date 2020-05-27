

from matplotlib import pyplot as plt
import numpy as np
import pandas as pd


peArray = [3.5, 4.5, 5, 2, 7]
tickerArray = ['a', 'b', 'c', 'd','e']

peArray_2020_04_15 = [14.45, 5.12, 6.98, 7.38, 9.10, 7.60, 12.47, 10.80, 10.16, 14.41, 14.40, 14.34, 13.89, 12.02, 16.60, 18.46, 18.75, 18.75, 25.55]
peArray_2020_04_14 = [10.45, 1.12, 7.98, 5.38, 8.10, 6.60, 12.47, 10.80, 10.16, 14.41, 14.40, 14.34, 13.89, 12.02, 16.60, 18.46, 18.75, 18.75, 25.55]

peArray = peArray_2020_04_15
tickerArray = ['ISF', 'CSRU', 'ITKY', 'SEDY', 'FXC', 'IDVY', 'EIMU', 'LTAM', 'IBZL', 'CSX5', 'EUE', 'CUKS', 'MIDD', 'DJSC', 'IWRD', 'NDIA', 'CSPX', 'IUSA', 'CNDX']

# put the data into a dataframe
#df = pd.DataFrame(columns=tickerArray, data=peArray)
#df = pd.DataFrame(index=tickerArray, data=peArray, columns=['pe ratio'])
df = pd.DataFrame({'ticker':tickerArray, 'pe':peArray, 'pe old':peArray_2020_04_14})
print('the dataframe')
print(df)


# gca stands for 'get current axis'
ax = plt.gca()

df.plot(kind='bar',x='ticker', y='pe', ax=ax)
df.plot(kind='bar',x='ticker', y='pe old', color='red', ax=ax)
plt.show()
# print(df.head())

# Return evenly spaced values within a given interval
npSize = np.arange(len(tickerArray))
size = range(len(peArray))

print(npSize+0.2)


plt.bar(npSize+0.2, peArray, width=0.4, color=(0,0,1,1))
plt.bar(npSize-0.2, peArray_2020_04_14, width=0.4, color=(1, 0, 0, 0.9))
plt.xticks(npSize,tickerArray)
plt.xticks(npSize,rotation='vertical')
plt.show()






