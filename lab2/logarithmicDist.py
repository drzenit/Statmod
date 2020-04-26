from math import log
import matplotlib.pyplot as plt
import seaborn as sns
from prettytable import PrettyTable
from scipy.special import beta

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

    def graphSimulationResult(self):
        sns.distplot(self.logList, hist=False, label='Practic results')
        plt.show()
        plt.title("Practic Histogram")
        plt.hist(self.logList, bins=50)
        plt.show()

    def graphProbabilityDensity(self):
        r = range(1, 11)
        p = list()
        for i in r:
            p.append(-(self.q)**i / (i * log(self.p)))
        plt.title("Probability Density")
        plt.vlines(r, ymin=p, ymax=0, colors="red")
        plt.plot(r, p, 'g')
        plt.show()

    def graphIntegralProbabilityDensity(self):
        x = range(1, 11)
        p = list()
        for i in x:
            p.append(1 + ((beta(i + 1, 1)) / log(1 - self.p)))
        plt.title("Integral Probability Density")
        plt.vlines(x, ymin=0, ymax=p, colors="red")
        plt.plot(x, p, 'g')
        plt.show()


n = 10000
a = LogarithmicDist(n, 0.5)

l = a.createLogList()

matExpec = commonFunc.getMathematicalExpectation(l, n)
print(l)
print(matExpec)
print(commonFunc.getDispersion(l, n, matExpec))

a.outputResult()
a.graphSimulationResult()
a.graphProbabilityDensity()
a.graphIntegralProbabilityDensity()