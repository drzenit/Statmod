import random
import matplotlib.pyplot as plt
from scipy.stats import uniform


# Генерация n случайных вещественных чисел [0,1]
def generateRandomList(n):
    randNumbList = list()
    for i in range(n):
        randNumbList.append(random.random())

    return randNumbList

# Построение функции плотности распределения
def graphProbabilityDensity(numbList):
    plt.plot(numbList, uniform.pdf(numbList))
    plt.show()

# Построение интегральной функции распределения
def graphIntegralProbabilityDensity(numbList):
    plt.plot(numbList, uniform.cdf(numbList))
    plt.show()