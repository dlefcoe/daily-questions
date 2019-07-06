
# coding: utf-8

# In[28]:


'''

This problem was asked by Stripe.
Given an array of integers, find the first missing positive integer in linear time and constant space. 
In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.
You can modify the input array in-place.

'''


arr = [3, 4, -1, 1]
arr.sort()


for e, val in enumerate(arr):
    if val <= 0:
        #look at next value
        continue
    elif val > 0:
        #now compare with next number
        if arr[e+1] - arr[e] >1:
            print('missing pos integer:',arr[e] + 1)            
        break
    else:
        print('wtf')



