'''


some code will go here...



'''

class Person:

    def __init__(self, name='firstname', age=25, platform='bumble', hairColour='blonde'):
        self.name = name #'clara'
        self.age = age #25
        self.platform = platform # 'bumble'
        self.hairColour = hairColour # 'blonde'



a = Person('clara', 20, 'bumble')
b = Person()
print(a.name)
print(b.name)

print(b.__dict__)

people = {'clara':a, 'nextperson':b}

print(people['clara'].age)

for i in people:
    print(people[i].age)


print('------------')

class Thing:

    def __init__(self, colour):
        self.colour = colour
        pass

    doit = 100
    bethere = 'london'

print(Thing.doit)

x = Thing('green')
y = Thing
y.doit = 101
y.bethere = 'tokyo'



class NameOfTheClass:
    ''' description of the class '''

    def __init__(self, a, b):
        self.a = a
        self.b = b

x = NameOfTheClass('green', 10)
print(x.__dict__)





