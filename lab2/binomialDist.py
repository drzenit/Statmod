import math
from math import factorial
import random

import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import binom
import seaborn as sns

from lab2 import commonFunc


class BinomialDist():
    def __init__(self, n: int, N: int, p: float, method: str):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.normNumbList = list()
        self.N = N
        self.p = p
        self.method = method
        self.binomList = self.createBinomList()

    def gaussian(self, x, mu, sigma):
        return math.exp(-0.5 * ((x - mu) / sigma) ** 2) / sigma / math.sqrt(2 * math.pi)

    def bernFunc(self):
        listP = list()
        for r in range(11):
            bernForm = (factorial(self.N) / (factorial(r) * factorial(self.N - r))) * (self.p**r) * ((1 - self.p)**(self.N - r))
            listP.append(bernForm)

        return listP

    def binomFunc(self):
        p0 = (1 - self.p)**self.N
        p = p0
        listP = list()
        listP.append(p)
        for r in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]:
            binomForm = p * (((self.N - r) / (r + 1)) * (self.p / (1 - self.p)))
            listP.append(binomForm)
            p = binomForm

        return listP

    def IRNBNL(self, randNum: float):
        P = self.bernFunc()
        M = randNum
        for x in range(11):
            M = M - P[x]
            if (M >= 0):
                continue
            elif (M < 0):
                return x

    def createBinomList(self):
        binomList = list()
        if (self.method == "BNL"):
            for i in self.numbList:
                IR = self.IRNBNL(i)
                if (IR != None):
                    binomList.append(IR)
        elif (self.method == "BIN"):
            for i in range(self.n):
                IR = round(random.normalvariate(5, 2.5) + 0.5)
                if (IR != None):
                    binomList.append(IR)

        return binomList

    def findMaxFrq(self):
        maxNumbList = list()
        maxFrqList = list()
        maxFrqList.append(1)
        for i in self.binomList:
            frqNumb = i
            if (frqNumb in maxNumbList):
                continue
            frq = 0
            for k in self.binomList:
                if (frqNumb == k):
                    frq += 1
            if (frq > maxFrqList[0]):
                maxNumbList.clear()
                maxFrqList.clear()
                maxNumbList.append(frqNumb)
                maxFrqList.append(frq)
            elif (frq == maxFrqList[0]):
                maxNumbList.append(frqNumb)
                maxFrqList.append(frq)

        return maxNumbList

    def outputResult(self, listBNL: list, listBIN: list):
        resultTable = PrettyTable()
        resultTable.field_names = ["Оценка", "IRBNL", "IRNBIN", "Теоретическое значение"]
        matExpecBNL = commonFunc.getMathematicalExpectation(listBNL, len(listBNL))
        dispersionBNL = commonFunc.getDispersion(listBNL, len(listBNL), matExpecBNL)
        matExpecBIN = commonFunc.getMathematicalExpectation(listBIN, len(listBIN))
        dispersionBIN = commonFunc.getDispersion(listBIN, len(listBIN), matExpecBIN)
        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpecBNL, dispersionBNL), "%f\n%f" % (matExpecBIN, dispersionBIN), "%f\n%f" % (5, 2.5)])
        print(resultTable)

    def graphBinomDist(self):
        #  Практика
        if (self.method == "BNL"):
            binsPar = 11
        elif (self.method == "BIN"):
            binsPar = 10
        fig, ax = plt.subplots(figsize=(14, 7))
        sns.distplot(self.binomList, bins = binsPar, label='simulation results')
        ax.set_xlabel("Number of Heads", fontsize=16)
        ax.set_ylabel("Frequency", fontsize=16)

        #  Теория
        x = range(0, 10)
        ax.plot(x, binom.pmf(x, 10, 0.5), 'ro', label='actual binomial distribution')
        ax.vlines(x, 0, binom.pmf(x, 10, 0.5), colors='r', lw=5, alpha=0.5)
        plt.legend()
        plt.show()

    def graphSimulationResult(self):
        sns.distplot(self.binomList, hist=False, label='Practic results')
        plt.show()
        plt.title("Practic Histogram")
        plt.hist(self.binomList, bins=50)
        plt.show()

    def graphProbabilityDensity(self):
        r = range(1, 11)
        p = list()
        for i in r:
            p.append((factorial(self.N) / (factorial(i) * factorial(self.N - i))) * (self.p**i) * ((1 - self.p)**(self.N - i)))
        plt.title("Probability Density")
        plt.vlines(r, ymin=p, ymax=0, colors="red")
        plt.plot(r, p, 'g')
        plt.show()

    def graphIntegralProbabilityDensity(self):
        x = range(1, 11)
        p = list()
        sumUni = 0
        for i in x:
            sumUni = sumUni + (factorial(self.N) / (factorial(i) * factorial(self.N - i))) * (self.p**i) * ((1 - self.p)**(self.N - i))
            p.append(sumUni)
        plt.title("Integral Probability Density")
        plt.vlines(x, ymin=0, ymax=p, colors="red")
        plt.plot(x, p, 'g')
        plt.show()


binomialDistBNL = BinomialDist(10000, 10, 0.5, "BNL")
binomialDistBIN = BinomialDist(10000, 10, 0.5, "BIN")

binomialDistBNL.outputResult(binomialDistBNL.binomList, binomialDistBIN.binomList)

binomialDistBNL.graphSimulationResult()
binomialDistBIN.graphSimulationResult()
binomialDistBNL.graphProbabilityDensity()
binomialDistBNL.graphIntegralProbabilityDensity()


