# Write your code here :-)
import random

numberOfStreaks = 0
potentialStreak = 0
listOfResults = []

for i in range(10000):
    # Generates a random integer starting from 0 to 1
    randomValue = random.randint(0, 1)
    if randomValue == 1:
        listOfResults.append('Heads')
    else:
        listOfResults.append('Tails')

    #//If new value is the same as the old value, potential streak +1, if potential streak is => 6 make numberOfStreaks + 1.
    # If current index of listOfResults == to the last one, add to potentialStreak. So if current 1 == old 1 it counts to the potential streak.
    if listOfResults[i] == listOfResults[i - 1]:
        potentialStreak += 1
        if potentialStreak >= 6:
            #When we get to 6, reset the counter back to 0.
            numberOfStreaks += 1
            potentialStreak = 0
    else:
        potentialStreak = 0


print('Chance of streak: %s%%' % (numberOfStreaks / 100))


