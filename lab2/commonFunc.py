import random


# Генерация n случайных вещественных чисел [0,1]
def generateRandomList(n):
    randNumbList = list()
    for i in range(n):
        randNumbList.append(random.random())

    return randNumbList

# Получение эмпирического математического ожидания
def getMathematicalExpectation(numbList: list, n: int):
    sumOfNumb = 0.0
    for i in numbList:
        sumOfNumb += i
    matExpec = sumOfNumb / (n - 1)

    return matExpec

# Получение эмпирической дисперсии
def getDispersion(numbList: list, n: int, matExpec: float):
    deviation = 0.0
    for i in numbList:
        deviation += ((i - matExpec) ** 2)
    dispersion = deviation / (n - 1)

    return dispersion
