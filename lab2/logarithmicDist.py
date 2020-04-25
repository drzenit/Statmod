from math import log
import sns as sns
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable
from scipy.stats import logser

from lab2 import commonFunc


class LogarithmicDist():
    def __init__(self, n: int, q: float):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.q = q
        self.p = 1 - q
        self.logList = self.createLogList()

    def getNextP(self, prevP: float, r: int):
        p = prevP * self.q / (r + 1) * r

        return p

    def IRNLOG(self, randNum: float):
        p0 = -self.q / log(self.p)
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

    def createLogList(self):
        logList = list()
        for i in self.numbList:
            IR = self.IRNLOG(i)
            if (IR != None):
                logList.append(IR)
        return logList

    def outputResult(self):
        resultTable = PrettyTable()
        resultTable.field_names = ["Момент", "IRNLOG", "Отклон", "Теоретическое значение"]
        matExpec = commonFunc.getMathematicalExpectation(self.logList, self.n)
        dispersion = commonFunc.getDispersion(self.logList, self.n, matExpec)

        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpec, dispersion), "%f\n%f" % ((1.44270 - matExpec), (0.80402 - dispersion)), "%f\n%f" % (1.44270, 0.80402)])
        print(resultTable)

    def graphLogDist(self):
        fig, ax = plt.subplots(figsize=(14, 7))
        sns.distplot(self.logList, label='simulation results')
        ax.set_xlabel("Number of Heads", fontsize=16)
        ax.set_ylabel("Frequency", fontsize=16)

        ax.plot(self.logList, logser.pmf(self.logList, 0.5), 'ro', label='actual binomial distribution')
        ax.vlines(self.logList, 0, logser.pmf(self.logList, 0.5), colors='r', lw=5, alpha=0.5)
        plt.legend()
        plt.show()


n = 100000
a = LogarithmicDist(n, 0.5)

l = a.createLogList()

matExpec = commonFunc.getMathematicalExpectation(l, n)
print(l)
print(matExpec)
print(commonFunc.getDispersion(l, n, matExpec))

a.outputResult()
a.graphLogDist()
