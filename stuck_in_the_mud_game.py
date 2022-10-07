'''
The game begins with the player 'rolling 5 dice.' 
Then the player gets a score of the combined numbers of the dice excluding 2's and 5's. 
Any 2's or 5's rolled results in dice "stuck in the mud." 
So say you roll a [1, 3, 4, 5, 2] the score should be: 8. 
Then the player rolls the remaining 3 dice, again you rolled [6,3,2] the score should then be 17. 
So on and so forth until the player runs out of dice and the code returns a final score.

'''


import random

score = 0
games_played = 0
number_rolls = 5

while True:
    games_played += 1
    if games_played > 100:
        print('more than 100 games played: you won !!!')
        break

    dice = [random.randint(1,6) for i in range(number_rolls)]
    dice = [d for d in dice if d in [1,3,4,6]]  # remove 2 & 5

    if len(dice) == 0:
        break

    for d in dice:
        score = score + d
        print('current score:', score)
        

print('---end---')
print('games played:', games_played)
print('final score', score)
