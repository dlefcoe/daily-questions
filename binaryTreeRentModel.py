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





class NodeOld:
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
            return f"{self.val}[{self.l},{self.r}]"
        return str(self.val)

    def getfairvalue(self):
        return self.l.val + self.r.val

    def createleft(self):
        self.l= NodeOld(NodeOld.rent * NodeOld.goodprob)

    def createright(self):
        self.r= NodeOld(NodeOld.shitrate * NodeOld.badprob)


root = NodeOld()

root.createleft()
root.createright()
root.val = root.getfairvalue()

# print(root)




class Monthly:
    ''' class for a node of the tree '''
    def __init__(self, val, goodTenant, contractedRent):
        '''
        val: [int] value of the node
        goodTenant: [bool] true or false for good or bad tenant
        prob: [float] the probability of getting paid
        up: [float] value of child node if paid
        dn: [float] value of child node if not paid
        recover: [float] the recovery %,  100% full paid, 0% not paid, 50% half paid
        '''
        self.goodTenant = goodTenant
        self.contractedRent = contractedRent
        self.val = val
        # set the probs and recoveries based on tenant type
        if self.goodTenant == True:
            self.prob = 0.99
            self.recoverUp = 1
            self.recoverDn = 0.25
            # these are the children nodes for good tenant
            self.up = self.contractedRent * self.prob * self.recoverUp
            self.dn = self.contractedRent * (1-self.prob) * self.recoverDn
        elif self.goodTenant == False:
            self.prob = 0.25
            self.recoverUp = 1.5
            self.recoverDn = 0.125
            # these are the children nodes for bad tenant
            self.up = self.contractedRent * self.prob * self.recoverUp
            self.dn = self.contractedRent * (1-self.prob) * self.recoverDn
        else:
            print('error, should not get here')

    
    def getPrev(self):
        pass
        return 100

    def calcUpMove(self):
        ''' calculate an upmove based on parent params '''
        self.up = self.contractedRent * self.prob * self.recoverUp 
        return self.up
    
    def calcDnMove(self):
        pass
        return

    



    



# set the root
tenantStart = True # assume tenant is good
contractedRent = 1000
startValue = contractedRent
root = Monthly(startValue, tenantStart, contractedRent)

print(f'good tenant: {root.goodTenant}, {round(root.up,4)}, {round(root.dn,4)}')



tenantStart = False # assume tenant is bad
contractedRent = 1000
startValue = contractedRent
root = Monthly(startValue, tenantStart, contractedRent)


print(f'bad tenant: {root.goodTenant}, {round(root.up,4)}, {round(root.dn,4)}')




"""
output is:
925.0[900.0,24.999999999999993]

"""