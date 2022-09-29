# %%  plot a function
import numpy as np
import matplotlib.pyplot as plt

def f(x): return 4*x**2 * np.exp(-2*x)
def g(x): return 4*x**2 * np.exp(-x)

x_values = np.linspace(0, 6, 100)
y = [f(x) for x in x_values]
plt.plot(x_values, y, label='f(x)')
y = [g(x) for x in x_values]
plt.plot(x_values, y, label='g(x)')

plt.title('f(x): exp(-2x), g(x):exp(-x)')
plt.xlabel('x values   -->')
plt.ylabel('f(x) -->')
plt.legend()
plt.show()

