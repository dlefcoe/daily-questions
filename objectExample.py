
# example of object

# the class is longer but more flexible
class aboutMe:
    ''' name of the person '''
    firstName = 'darren'
    secondName = 'test'

    def __init__(self, a, b):
        self.a = a
        self.b = b



print(aboutMe.firstName)



# the dict is smaller and faster
myDict = {"name":'darren', "age":25}
print(myDict['name'])




# the class lets the user invoke the . notation
hello = 'hello ' + aboutMe.firstName
print(hello)