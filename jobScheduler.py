# -*- coding: utf-8 -*-
"""
Created on Thu Jul 11 19:14:43 2019
@author: Owner

This problem was asked by Apple.
Implement a job scheduler which takes in a function f and an integer n, and calls f after n milliseconds.

"""


print('running code...')

i = 1

import sched, time
s = sched.scheduler(time.time, time.sleep)
def do_something(i, nonceTest): 
    print("Doing stuff..." + str(i) + " " + nonceTest)
    # do your stuff
    #s.enter(10, 1, do_something, (sc,))



# run every x seconds, for a specified number of times.
def scheduleIt(everyX_Sec, numberOfTimes):
    for i in range(numberOfTimes):        
        s.enter(everyX_Sec * i, 1, do_something, argument =(i, "...completed"))
    s.run()

scheduleIt(2, 5)


print('code completed !')

