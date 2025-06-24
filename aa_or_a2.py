

import random
import statistics

break_list = []
end_count = 0
for j in range(1000):
    for i in range(10_000):
        a = random.uniform(0,1)
        b = a*a
        c = a**2

        if c != b:
            # print(i)
            # print(a, c, b)
            break_list.append(i)
            break
        if i == 9_999:
            end_count = end_count + 1
# print(break_list)
print(f'end count: {end_count}')
print('average break:',  statistics.mean(break_list))
print('std break', statistics.stdev(break_list))
# print('end')


print('--- the end ---')



