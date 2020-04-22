from prettytable import PrettyTable

from lab2 import commonFunc


class UniformDist:
    def __init__(self, n: int, lowLimit: int, upLimit: int):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.lowLimit = lowLimit
        self.upLimit = upLimit

    def createIntList(self):
        intNumbList = list()
        for i in self.numbList:
            IR = commonFunc.IRNUNI(self.lowLimit, self.upLimit, i)
            intNumbList.append(IR)

        return intNumbList

    def getMathematicalExpectation(self):
        sumOfNumb = 0.0
        for i in self.numbList:
            sumOfNumb += i
        matExpec = sumOfNumb / (self.n - 1)

        return matExpec

    def getDispersion(self, matExpec: float):
        deviation = 0.0
        for i in self.numbList:
            deviation += ((i - matExpec) ** 2)
        dispersion = deviation / (self.n - 1)

        return dispersion

    def outputResult(self):
        resultTable = PrettyTable()
        resultTable.field_names = ["Оценка", "IRNUNI", "Погрешность", "Теоретическое значение"]
        numbList = self.createIntList()
        matExpec = self.getMathematicalExpectation(numbList, self.n)
        dispersion = self.getDispersion(numbList, matExpec, self.n)

        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpec, dispersion), "%f\n%f" % ((50.5 - matExpec), (833.25 - dispersion)), "%f\n%f" % (50.5, 833.25)])
        print(resultTable)


uniformDist = UniformDist(10000, 1, 100)

uniformDist.outputResult()