"""
How many people need to be in a room for there to be a 50/50 chance that two of them
share the same birth month and day?
1 Use MCS to determine how many people it takes to reach the 50 percent mark.
2 Have the program print out the number of people and the probability for a range of room
occupants.
3 If you find yourself looking up how to format dates, stop and simplify!

Input variables = participants` birthdays
Probability distribution = uniform(1/365 for each participant)
While probability < 50
    increase participant number
    Loop2:
        Loop3: randomly select dates for participants and append to birth_list
        Calculation = group the same dates with Counter and
                      increase success by 1 if group consists of two or more
        Repeat = 1000 times
    Aggregate: divide success by repeat times
"""
from random import randint
from collections import Counter

n = 30 # max participant number
repeats = 100


for m in range(2, n):

    success = 0
    for repeat in range(repeats+1):

        birth = []
        for i in range(m+1):
            birth_d = randint(1, 365)
            birth.append(birth_d)

        coincide = Counter(birth)
        val_coincide = Counter(coincide.values())
        success += val_coincide[2]

    probability = 1 - success/(m*repeats)
    print("probability of coincidence = {}%".format(probability))

    if probability < 50:
        break

