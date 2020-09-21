import matplotlib.pyplot as plt
from prettytable import PrettyTable
import seaborn as sns

import commonFunc


class UniformDist:
    def __init__(self, n: int, lowLimit: int, upLimit: int):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.lowLimit = lowLimit
        self.upLimit = upLimit
        self.uniformList = self.createUniformList()

    def IRNUNI(self, ILOW: int, IUP: int, floatNum: float):
        r = (IUP - ILOW + 1) * floatNum + ILOW

        return round(r)

    def createUniformList(self):
        intNumbList = list()
        for i in self.numbList:
            IR = self.IRNUNI(self.lowLimit, self.upLimit, i)
            intNumbList.append(IR)

        return intNumbList

    def outputResult(self):
        resultTable = PrettyTable()
        resultTable.field_names = ["Оценка", "IRNUNI", "Погрешность", "Теоретическое значение"]
        matExpec = commonFunc.getMathematicalExpectation(self.uniformList, self.n)
        dispersion = commonFunc.getDispersion(self.uniformList, self.n, matExpec)

        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpec, dispersion), "%f\n%f" % ((50.5 - matExpec), (833.25 - dispersion)), "%f\n%f" % (50.5, 833.25)])
        print(resultTable)

    def graphSimulationResult(self):
        sns.distplot(self.uniformList, hist=False, label='Practic results')
        plt.show()
        plt.title("Practic Histogram")
        plt.hist(self.uniformList, bins=200)
        plt.show()

    def graphProbabilityDensity(self):
        p = 1 / (self.upLimit - self.lowLimit + 1)
        x = range(self.lowLimit, self.upLimit)
        pLine = list()
        for i in x:
            pLine.append(p)
        plt.title("Probability Density")
        plt.vlines(x, ymin=p, ymax=0, colors="red")
        plt.plot(x, pLine, 'g')
        plt.show()

    def graphIntegralProbabilityDensity(self):
        x = range(self.lowLimit, self.upLimit)
        p = list()
        for i in x:
            p.append(i - self.lowLimit + 1 / (self.upLimit - self.lowLimit + 1))
        plt.title("Integral Probability Density")
        plt.vlines(x, ymin=0, ymax=p, colors="red")
        plt.plot(x, p, 'g')
        plt.show()
