# %% prime slopes
import math
import matplotlib.pyplot as plt


def gen_primes(n):
    """ Returns  a list of primes < n """
    sieve = [True] * n
    for i in range(3,int(n**0.5)+1,2):
        if sieve[i]:
            sieve[i*i::2*i]=[False]*((n-i*i-1)//(2*i)+1)
    return [2] + [i for i in range(3,n,2) if sieve[i]]

n = 1_000
prm_list = gen_primes(n)
prm_list = [x*math.sin(x/100) for x in prm_list]

x_values = []
prm_slopes = []  # generate prime slopes
for i, v in enumerate(prm_list[1:]):
    prm_slopes.append(v-prm_list[i])
    x_values.append(i)

null_slopes = [i for i,v in enumerate(prm_slopes) if -5 < v < 5 ]


print('null slopes:', null_slopes)
print('max slope:', max(prm_slopes))

x_values_second = []
prm_second_slopes = []  # generate second derivative
for i, v in enumerate(prm_slopes[1:]):
    prm_second_slopes.append(v-prm_slopes[i])
    x_values_second.append(i)

null_second_slopes = [i for i,v in enumerate(prm_second_slopes) if -1 < v < 1 ]


fig, ax = plt.subplots()

plt.title('sin*primes with signals')
plt.xlabel('order (x=1 to n)')
plt.ylabel('prime')
plt.grid()
ax.plot(prm_list, label='sin*primes')
ax2 = ax.twinx()
ax2.axhline(y=0, color='orange')
for i in null_slopes:
    ax2.axvline(x=i, color='orange')
for i in null_second_slopes:
    ax2.axvline(x=i, color='yellow')


ax2.plot(x_values, prm_slopes, linestyle='solid', color='red', label='1st slopes')
ax2.plot(x_values_second, prm_second_slopes, linestyle='solid', color='yellowgreen', label='2nd slopes')

plt.legend(loc=2)

plt.show()
