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



thing = 'fuck on bonet of car'
ideaDate = datetime.date(2019, 12, 21)
completedDate = datetime.date(2019, 12, 21)


todoList.append(todoItems(thing, ideaDate, completedDate))


print(todoList[0].__dict__)


completedList = []

completedList.append('meet wearing only coat and heels')
completedList.append('fuck in room')
completedList.append('blow job in room')
completedList.append('lick pussy in room')
completedList.append('press up against wall and fuck')
completedList.append('press up against wall and fuck')
completedList.append('press up against wall and fuck')
completedList.append('press up against wall and fuck')

completedList.append('whip ass')
completedList.append('slap ass')

completedList.append('fuck on the floor')

completedList.append('fuck in hotel toilets')


print(completedList)

