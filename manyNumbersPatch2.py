import random

def randomGenerator(minRange, maxRange, amount):
    list = []
    for i in range(amount):
        list.append(random.randint(minRange, maxRange))
    return list

amount = int(input())
minRange = int(input())
maxRange = int(input())
print(randomGenerator(amount, minRange, maxRange))
