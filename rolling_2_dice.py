# %%

'''
rolling 2 dice
plot a chart of all the outcomes

'''

from matplotlib import pyplot as plt

x, d = [], {}
for i in range(1,7):
    for j in range(1,7):
        x.append((i,j))
        s = i+j
        if s in d.keys(): d[s] = d[s] + 1
        else: d[s] = 1 

# print the data & results
print('dice rolls:\n', x, '\n')
print('results tally:', d)
print('number of outcomes:', sum(d.values()))

plt.bar(d.keys(),d.values())
plt.show()

