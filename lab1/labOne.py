import random
from math import sqrt
import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.stats import uniform
from statsmodels.graphics.tsaplots import plot_pacf
from prettytable import PrettyTable


# Задание 1: Генерация n псевдослучайных чисел на интервале [0,1]
def generateRandomList(n):
    randNumbList = list()
    for i in range(n):
        randNumbList.append(random.random())

    return randNumbList

# Задание 2.1: Вычисление математического ожидания
def getMathematicalExpectation(numbList, n):
    sumOfNumb = 0.0
    for i in numbList:
        sumOfNumb += i
    matExpec = sumOfNumb / (n - 1)

    return matExpec

# Задание 2.1: Вычисление дисперсии
def getDispersion(numbList, matExpec, n):
    deviation = 0.0
    for i in numbList:
        deviation += ((i - matExpec)**2)
    dispersion = deviation / (n - 1)

    return dispersion

# Задание 2.3: Вычисление Среднеквадратического отклонения
def getStandardDeviation(dispersion):
    standDeviation = sqrt(dispersion)

    return standDeviation

# Задание 3.1: Вычисление значений автокорреляционной функции
def getAutocorrelation(numbList, matExpec, n):
    autocorrList = list()
    for f in range(1, n):
        upAutocorr = 0.0
        downAutocorr = 0.0
        i = 0
        while (i < (n - 1 - f)):
            upAutocorr += ((numbList[i] - matExpec) * (numbList[i + f] - matExpec))
            i += 1
        i = 0
        while (i < (n - 1)):
            downAutocorr += ((numbList[i] - matExpec)**2)
            i += 1
        autocorrVal = (upAutocorr / downAutocorr)
        autocorrList.append(autocorrVal)

    return  autocorrList

# Задание 3.2: Построение коррелограммы
def grapgColerrogram(autoCorr, lagsPar):
    plot_pacf(autoCorr, lags=lagsPar, alpha=None)  # Функция из изменена, коррелограмма строиться по полученным значениям autoCorr
    pyplot.show()

# Задание 4.1: Построение функции плотности распределения
def graphProbabilityDensity(numbList):
    plt.plot(numbList, uniform.pdf(numbList))
    plt.show()

# Задание 4.2: Построение интегральной функции распределения
def graphIntegralProbabilityDensity(numbList):
    plt.plot(numbList, uniform.cdf(numbList))
    plt.show()

# Вывод результатов в таблицу
def outputResult():
    resultTable = PrettyTable()
    resultTable.field_names = ["n", "Оценка распр.", "RAND эксперимент", "Теоретическое значение", "Отклонение"]

    for n in (10, 100, 1000, 10000):
        numbList = generateRandomList(n)
        matExpec = getMathematicalExpectation(numbList, n)
        dispersion = getDispersion(numbList, matExpec, n)

        resultTable.add_row([n, "M = \n D = ", "%f\n%f" % (matExpec, dispersion), "%f\n%f" % (0.5, 0.08333),
                             "%f\n%f" % ((0.5 - matExpec), (0.08333 - dispersion))])
    print(resultTable)


# Выполнение программы

numbList = generateRandomList(10001)
matExpec = getMathematicalExpectation(numbList, 10001)
dispersion = getDispersion(numbList, matExpec, 10001)
deviation = getStandardDeviation(dispersion)
autocorr = getAutocorrelation(numbList, matExpec, 10001)

graphProbabilityDensity(numbList)
graphIntegralProbabilityDensity(numbList)
grapgColerrogram(autocorr, (10000 - 1))

outputResult()

print("\n Среднее квадратическое отклонение = ", deviation)
