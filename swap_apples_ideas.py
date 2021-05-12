'''

if you swap apples then you dont gain anything
but if you swap ideas, then you gain ideas


'''





def main():
    person1 = Person(5, 3)
    person2 = Person(1, 2)

    # swap apples
    person1.apples, person2.apples = person2.apples, person1.apples

    # swap ideas
    person1.ideas = person1.ideas + person2.ideas
    person2.ideas = person1.ideas
    print(person1)
    print(person2)


class Person:
    ''' description of the class '''

    def __init__(self, apples, ideas):
        '''
        apples (int): number of apples
        ideas (int): number of ideas
        '''
        self.apples = apples
        self.ideas = ideas


    def __repr__(self):
        '''represent the class's objects as a string'''
        return f'Person({self.apples},{self.ideas})'







if __name__=='__main__':
    ''' This is executed when run from the command line '''
    main()