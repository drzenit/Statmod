from math import exp, factorial
from random import random
import matplotlib.pyplot as plt
from prettytable import PrettyTable
import seaborn as sns

from lab2 import commonFunc


class PoissonDist():
    def __init__(self, n: int, mu: int, method: str):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.mu = mu
        self.method = method
        self.poissList = self.createPoissList()

    def IRNUNI(self, ILOW: int, IUP: int, floatNum: float):
        r = (IUP - ILOW + 1) * floatNum + ILOW

        return round(r)

    def getNextP(self, prevP: float, r: int):
        p = prevP * self.mu / r

        return p

    def getPrevP(self, p: float, r: int):
        p = p * r / self.mu

        return p

    def getQ(self):
        p = exp(-self.mu)
        Q = p
        Pl = p
        x = 1
        l = x
        pNext = self.getNextP(p, x)
        while (p <= pNext):
            Pl = pNext
            l = x
            Q = Q + pNext
            p = pNext
            x += 1
            pNext = self.getNextP(p, x)

        return Q, l, Pl

    def IRNPOI(self, randNum: float):  # слишком доооолго
        p0 = exp(-self.mu)
        P = p0
        M = randNum
        x = 1
        while (True):
            M = M - P
            if (M >= 0):
                x += 1
                P = self.getNextP(P, x)
                continue
            elif (M < 0):
                return x

    def IRNPSN(self):
        r = 0
        mul = 1
        while (mul >= exp(-self.mu)):
            u = random()
            r += 1
            mul = mul * u
        return r


    def specAlgorithm(self, randNum: float):
        Q = self.getQ()
        M = randNum - Q[0]
        m = Q[1]
        P = Q[2]
        if (M >= 0):
            while (True):
                P = self.getNextP(P, m)
                M = M - P
                if (M <= 0):
                    return m
                else:
                    m += 1
        else:
            while (True):
                M = M + P
                if (M >= 0):
                    return m
                else:
                    P = self.getPrevP(P, m)
                    m -= 1


    def createPoissList(self):
        poissList = list()
        if (self.method == "POI"):
            for i in self.numbList:
                IR = self.IRNPOI(i)
                if (IR != None):
                    poissList.append(IR)
        elif (self.method == "SPEC"):
            for i in self.numbList:
                IR = self.specAlgorithm(i)
                if (IR != None):
                    poissList.append(IR)
        elif (self.method == "PSN"):
            for i in self.numbList:
                IR = self.IRNPSN()
                if (IR != None):
                    poissList.append(IR)

        return poissList

    def outputResult(self, listPOI: list, listPSN: list):
        resultTable = PrettyTable()
        resultTable.field_names = ["Момент", "IRNPOI", "IRNPSN", "Теоретическое значение"]
        matExpecPOI = commonFunc.getMathematicalExpectation(listPOI, len(listPOI))
        dispersionPOI = commonFunc.getDispersion(listPOI, len(listPOI), matExpecPOI)
        matExpecPSN = commonFunc.getMathematicalExpectation(listPSN, len(listPSN))
        dispersionPSN = commonFunc.getDispersion(listPSN, len(listPSN), matExpecPSN)
        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpecPOI, dispersionPOI), "%f\n%f" % (matExpecPSN, dispersionPSN), "%f\n%f" % (10.0, 10.0)])
        print(resultTable)

    def graphSimulationResult(self):
        sns.distplot(self.poissList, hist=False, label='Practic results')
        plt.show()
        plt.title("Practic Histogram")
        plt.hist(self.poissList, bins=50)
        plt.show()

    def graphProbabilityDensity(self):
        r = range(1, 25)
        p = list()
        for i in r:
            p.append((self.mu**i * exp(-self.mu)) / factorial(i))
        plt.title("Probability Density")
        plt.vlines(r, ymin=p, ymax=0, colors="red")
        plt.plot(r, p, 'g')
        plt.show()

    def graphIntegralProbabilityDensity(self):
        x = range(1, 40)
        p = list()
        sumPoi = 0
        for i in x:
            for k in range(i):
                sumPoi = sumPoi + ((self.mu**k * exp(-self.mu)) / factorial(k))
            p.append(sumPoi)
            sumPoi = 0
        plt.title("Integral Probability Density")
        plt.vlines(x, ymin=0, ymax=p, colors="red")
        plt.plot(x, p, 'g')
        plt.show()

poissonDistPSN = PoissonDist(10000, 10, "PSN")
poissonDistPOI = PoissonDist(10000, 10, "SPEC")

print(poissonDistPSN.poissList)


poissonDistPOI.outputResult(poissonDistPOI.poissList, poissonDistPSN.poissList)

poissonDistPOI.graphSimulationResult()
poissonDistPSN.graphSimulationResult()
poissonDistPSN.graphProbabilityDensity()
poissonDistPSN.graphIntegralProbabilityDensity()

