from math import exp

import sns as sns
import matplotlib.pyplot as plt
from prettytable import PrettyTable
from scipy.stats import poisson
import seaborn as sns

from lab2 import commonFunc


class PoissonDist():
    def __init__(self, n: int, mu: int, method: str):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.mu = mu
        self.method = method
        #self.poissList = self.createPoissList()

    def IRNUNI(self, ILOW: int, IUP: int, floatNum: float):
        r = (IUP - ILOW + 1) * floatNum + ILOW

        return round(r)

    def getNextP(self, prevP: float, r: int):
        p = (prevP * self.mu) / r

        return p

    def IRNPOI(self, randNum: float):
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

    def IRNPSN(self, randNum: float):
        poiList = list()
        poiNum = 1
        for i in self.numbList:
            if (poiNum >= exp(-self.mu)):
                poiNum = poiNum * i
            poiList.append(self.IRNUNI(poiNum, 1, 6))
            poiNum = 1

        return poiList


a = PoissonDist(10000, 10, "1")

print(a.IRNPSN(2.1))

print(commonFunc.getMathematicalExpectation(a.IRNPSN(2.1), 10000))

