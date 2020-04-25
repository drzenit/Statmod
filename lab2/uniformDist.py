import matplotlib.pyplot as plt
from prettytable import PrettyTable
import seaborn as sns
from scipy.stats import uniform

from lab2 import commonFunc


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

    def graphHist(self):
        plt.hist(self.uniformList)
        plt.show()


uniformDist = UniformDist(10000, 1, 100)

uniformDist.outputResult()
uniformDist.graphHist()
