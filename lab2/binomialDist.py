import random

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

print(a.binomList)

#print(a.findMaxFrq())

#  Практика
fig, ax = plt.subplots(figsize=(14,7))
sns.distplot(a.binomList, bins=11, label='simulation results')
ax.set_xlabel("Number of Heads",fontsize=16)
ax.set_ylabel("Frequency",fontsize=16)


#  Теория
x = range(0, 10)
ax.plot(x, binom.pmf(x, 10, 0.5), 'ro', label='actual binomial distribution')
ax.vlines(x, 0, binom.pmf(x, 10, 0.5), colors='r', lw=5, alpha=0.5)
plt.legend()
plt.show()


def testFunc(N: int, p = 0.5):
    a0 = (1 - p)**N
    b = a0
    listN = list()
    listN.append(a0)
    for r in [1, 2, 3, 4, 5, 6, 7, 8, 9]:
        a = b * (((N-r)/(r+1))*(p/(1-p)))
        listN.append(a)
        b = a
    return listN

