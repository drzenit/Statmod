from math import factorial
import sns as sns

from lab2 import commonFunc

import matplotlib.pyplot as plt
from matplotlib import pyplot
from scipy.stats import binom, norm
import seaborn as sns
from statsmodels.graphics.tsaplots import plot_pacf

class BinomialDist():
    def __init__(self, n: int, N: int, p: float):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.N = N
        self.p = p
        self.binomList = list()
        for i in self.numbList:
            self.binomList.append(commonFunc.IRNUNI(0, self.N - 1, i))

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

    def IRNBIN(self, randNum: float):
        P = self.binomFunc()
        M = randNum
        for x in range(11):
            M = M - P[x]
            if (M >= 0):
                continue
            elif (M < 0):
                return x

    def createBinomList(self, method: str):
        binomList = list()
        if (method == "BNL"):
            for i in self.numbList:
                IR = self.IRNBNL(i)
                if (IR != None):
                    binomList.append(IR)
        elif (method == "BIN"):
            for i in self.numbList:
                IR = self.IRNBIN(i)
                if (IR != None):
                    binomList.append(IR)

        return binomList

    def findMaxFrq(self):
        maxNumbList = list()
        maxFrqList = list()
        maxFrqList.append(1)
        for i in range(self.n):
            frqNumb = self.binomList[i]
            if (frqNumb in maxNumbList):
                continue
            frq = 0
            for k in range(self.n):
                if (frqNumb == self.binomList[k]):
                    frq += 1
            if (frq > maxFrqList[0]):
                maxNumbList.clear()
                maxFrqList.clear()
                maxNumbList.append(frqNumb)
                maxFrqList.append(frq)
            elif (frq == maxFrqList[0]):
                maxNumbList.append(frqNumb)
                maxFrqList.append(frq)

        return maxNumbList, maxFrqList


a = BinomialDist(10000, 10, 0.5)

print(a.binomFunc())
print(a.bernFunc())
print(a.createBinomList("BNL"))
print(len(a.createBinomList("BNL")))

#  Практика
fig, ax = plt.subplots(figsize=(14,7))
sns.distplot(a.createBinomList("BNL"), bins=11, label='simulation results')
ax.set_xlabel("Number of Heads",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)


#  Теория
x = range(0, 10)
ax.plot(x, binom.pmf(x, 10, 0.5), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, 10, 0.5), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()

