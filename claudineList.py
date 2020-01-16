'''

to do list with claudine.

'''

import datetime


# define blank list
todoList = []



class todoItems:
    # items for the list of things todo

    def __init__(self, thing, ideaDate, completedDate):
        self.thing = thing
        self.ideaDate = ideaDate
        self.completedDate = completedDate



thing = 'f on bonet of car'
ideaDate = datetime.date(2019, 12, 21)
completedDate = datetime.date(2019, 12, 21)


todoList.append(todoItems(thing, ideaDate, completedDate))


print(todoList[0].__dict__)


completedList = []

completedList.append('meet w only coat and h')
completedList.append('f in room')
completedList.append('b w in room')
completedList.append('l p in room')
completedList.append('press up against wall and f')
completedList.append('press up against wall and f')
completedList.append('press up against wall and f')
completedList.append('press up against wall and f')

completedList.append('wh a')
completedList.append('sl a')

completedList.append('f on the floor')

completedList.append('f in hotel t')


print(completedList)

