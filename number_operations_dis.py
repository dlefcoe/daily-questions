'''

which is more efficient?
   1. nested if
   2. and statement

answer:
  both take the same number of operations.
'''



import dis

def test_inner_if(condition1=True, condition2=True):
     if condition1:
         if condition2:
             pass
         
def test_and_if(condition1=True, condition2=True):
     if condition1 and condition2:
         pass
     
print('testing nested...')
dis.dis(test_inner_if)

print('testing and...')
dis.dis(test_and_if)
