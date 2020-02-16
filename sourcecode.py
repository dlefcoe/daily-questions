'''

module to get the source code of another module

'''


import inspect
from queue import Queue



x = inspect.getsource(Queue)
print(x)

