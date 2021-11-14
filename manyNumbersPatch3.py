import random as ran


amount = int(input('Amount of random numbers you want: '))
minRange = int(input('lowest number possible: '))
maxRange = int(input('highest number possible: '))

class randomGen():
    def randomGenerator(amount, minRange, maxRange):
        list = []
        for i in range(amount):
            list.append(ran.randint(minRange, maxRange))
        return list


    print(randomGenerator(amount, minRange, maxRange))


randomGen()
