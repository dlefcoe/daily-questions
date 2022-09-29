# %% desiese dynamics
import random
import matplotlib.pyplot as plt

# community of size n
num_people = 100_000
community = [x for x in range(num_people)]
community_noifications = []

class Person:

    def __init__(self, id=0) -> None:
        ''' base conditions of a person to start '''
        self.id = id  # unique id
        self.friends = self.generate_friends()
        self.motivation = 90  # motivation to transmit info
        self.aware = False  # is the person aware
        self.care = False   # if aware, does the person care
        self.notified = 0  # counter for times notiifed
        self.message_sent = 0  # counter for messages sent
        return
        
    def generate_friends(self) -> list:
        ''' generate a list of friends from the community '''
        friends = random.choices(community, k=5)
        friends = list(set(friends))
        return friends

    def update_person(self):
        ''' update the persons status '''
        self.notified += 1
        if self.notified > 1:
            self.motivation = self.motivation - 10

        if self.aware == False:
            # just heard rumour, now spread it.
            self.aware = True
            self.care = True
        
        if self.notified > 3:
            # now bored so dont care
            self.care = False

        return

    def message_friends(self, community_noifications:list):
        ''' message friends making them aware '''

        if self.aware == True and self.care== True:
            self.message_sent += 1
            self.motivation = self.motivation - 10
            if self.message_sent > 10:
                # sent enough messages, now bored
                self.care = False

            for i in self.friends:
                if self.motivation > random.randint(0,400):
                    community_noifications.append(i)
                
        

            

# generate a list of people
person = [Person(x) for x in community]

# a few people start a rumour
x = random.choices(community, k=3)
for i in x: 
    person[i].aware = True
    person[i].care = True
    person[i].notified = 1

# do some loops
who_is_aware = 0
who_cares = 0
community_aware = []
community_care = []
community_motivation = []

for i in range(40):
    # each aware person notifies friends
    for j in person:
        j.message_friends(community_noifications)

    # the people recieve notifications
    for j in community_noifications:
        person[j].update_person()

    # updates complete, so empty the list     
    community_noifications = [] 

    # collect the data from each loop
    who_is_aware = 0
    who_cares = 0
    motivation_level = 0
    for i in person:
        if i.aware == True:
            who_is_aware += 1
        if i.care ==True:
            who_cares += 1
        motivation_level = motivation_level + i.motivation/100
    community_aware.append(who_is_aware)
    community_care.append(who_cares)
    community_motivation.append(motivation_level)


print('done')
print(community_aware)
print(community_care)

plt.plot(community_motivation, label='community motivation')
plt.plot(community_aware, label='community aware')
plt.plot(community_care, label='community care', linewidth=4)

plt.title('who is aware and who cares')
plt.xlabel(' iteration ->')
plt.ylabel('count ->')
plt.legend()
plt.grid()
plt.show()



# plt.title('motivation levels')
# plt.xlabel(' iteration ->')
# plt.ylabel('motivation ->')
# plt.legend()
# plt.show()



