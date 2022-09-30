# a 2d graphics module
import turtle as ttl
import random
from scipy.stats import skewnorm
import matplotlib.pyplot as plt


ttl.shape('turtle')
ttl.speed(0)

def tree(size, levels):
    angle = random.choice(skewed_list(-30, x_low=10, x_high=30))

    if levels==0:
        if angle > 15:
            angle_colour = 'green'
        else:
            angle_colour = 'red'
        ttl.color(angle_colour)
        ttl.dot(size / 2)
        ttl.color('black')
        return

    if angle > 60:
        size = size * 1.2

    ttl.forward(size)
    ttl.right(angle)

    tree(size*0.8, levels-1)

    ttl.left(angle * 2.5)
    tree(size*0.8, levels-1)

    ttl.right(angle)
    ttl.backward(size)


def skewed_list(skew, size=1000, x_low=30, x_high=120):
    ''' returns a skewed list between x_low and x_high '''
    data= skewnorm.rvs(skew, size=size)*100
    data = data - min(data)
    data = data / max(data)
    data = data * x_high
    data = [x for x in data if x > x_low]

    return data

for i in range(7):
    # draw several trees
    ttl.left(90)
    tree_size = random.choice(skewed_list(-30, x_low=50, x_high=80))
    tree_levels = random.choice([7,8,9,10])
    tree(tree_size, tree_levels)
    # move to new random location
    ttl.right(90)
    ttl.penup()
    n = random.randint(0,360)
    ttl.right(n)
    ttl.forward(random.randint(1,5)*10 + 30)
    ttl.left(n)
    ttl.pendown()

ttl.mainloop()


print('done')
