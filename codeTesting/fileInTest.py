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