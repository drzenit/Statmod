import random


# Генерация n случайных вещественных чисел [0,1]
def generateRandomList(n):
    randNumbList = list()
    for i in range(n):
        randNumbList.append(random.random())

    return randNumbList
