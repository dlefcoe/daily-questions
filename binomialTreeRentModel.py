'''
author: darren**2
date: 2019

rent model.

there exists a situation where a tenant renting a property can either pay their rent, u, with a probability P
or can only pay part of the rent, d, with a probability (1-p).

We work out the fair value, v of the rent as follows:
v = [u * p] + [d * (1-p)]

given one can assume the fair value v and a probability of getting paid for the period
construct a binomial tree that computed the child legs.

the function would be
f(v, p) returns u, d

step 2:
assuming we know the outcomes
compute (and store) the next values on the tree

'''


class Node:
    """Class to represent a node."""

    goodprob = 0.9
    badprob = 1 - goodprob
    rent = 1000
    shitrate = 250

    def __init__(self, val=None, l=None, r=None):
        self.val = val
        self.l = l
        self.r = r

    def __repr__(self):
        # """Define output of print function."""
        if self.l or self.r:
            return (f"{self.val}[{self.l},{self.r}]")
        return str(self.val)

    def getfairvalue(self):
        return self.l.val + self.r.val

    def createleft(self):
        self.l= Node(Node.rent * Node.goodprob)

    def createright(self):
        self.r= Node(Node.shitrate * Node.badprob)


root = Node()

root.createleft()
root.createright()
root.val = root.getfairvalue()

print(root)


"""
output is:
925.0[900.0,24.999999999999993]

"""