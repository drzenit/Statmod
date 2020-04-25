from math import exp, factorial

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

    def IRNPSN(self, randNum: float):
        poiList = list()
        poiNum = 1
        for i in self.numbList:
            if (poiNum >= exp(-self.mu)):
                poiNum = poiNum * i
            poiList.append(self.IRNUNI(poiNum, 1, 6))
            poiNum = 1

        return poiList

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
                    return  m
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
                IR = self.IRNPSN(i)
                if (IR != None):
                    poissList.append(IR)

        return poissList


a = PoissonDist(10000, 10, "PSN")

matExpec = commonFunc.getMathematicalExpectation(a.IRNPSN(1), len(a.IRNPSN(1)))
print(matExpec)
print(commonFunc.getDispersion(a.IRNPSN(1), len(a.IRNPSN(1)), matExpec))


#print(commonFunc.getMathematicalExpectation(a.createPoissList(), 100))

