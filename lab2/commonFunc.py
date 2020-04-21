import random


# Генерация n случайных вещественных чисел [0,1]
def generateRandomList(n):
    randNumbList = list()
    for i in range(n):
        randNumbList.append(random.random())

    return randNumbList

def IRNUNI(ILOW: int, IUP: int, floatNum: float):
    r = (IUP - ILOW + 1) * floatNum + ILOW

    return round(r)
