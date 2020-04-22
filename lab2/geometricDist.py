from math import log

from prettytable import PrettyTable

from lab2 import commonFunc


class GeometricDist():
    def __init__(self, n: int, p: float, method: str):
        self.n = n
        self.p = p
        self.method = method
        self.numbList = commonFunc.generateRandomList(self.n)
        self.geomList = self.createGeomList()

    def IRNUNI(self, ILOW: int, IUP: int, floatNum: float):
        r = (IUP - ILOW + 1) * floatNum + ILOW

        return round(r)

    def getNextP(self, prevP: float):
        p = prevP * (1 - self.p)

        return p

    def IRNGEO_1(self, randNum: float):
        p0 = self.p
        P = p0
        M = randNum
        x = 1
        while(True):
            M = M - P
            if (M >= 0):
                x += 1
                P = self.getNextP(P)
                continue
            elif (M < 0):
                return x

    def IRNGEO_2(self, randNum: float):
        if (randNum <= self.p):
            intNum = self.IRNUNI(1, 10, randNum)  # Какие границы?

            return intNum

    def IRNGEO_3(self, randNum: float):
        k = (int(log(randNum) / log(1 - self.p))) + 1

        return k

    def createGeomList(self):
        geomList = list()
        if (self.method == "1"):
            for i in self.numbList:
                IR = self.IRNGEO_1(i)
                if (IR != None):
                    geomList.append(IR)
        if (self.method == "2"):
            for i in self.numbList:
                IR = self.IRNGEO_2(i)
                if (IR != None):
                    geomList.append(IR)
        if (self.method == "3"):
            for i in self.numbList:
                IR = self.IRNGEO_3(i)
                if (IR != None):
                    geomList.append(IR)

        return geomList

    def outputResult(self, list1: list, list2: list, list3: list):
        resultTable = PrettyTable()
        resultTable.field_names = ["Момент", "IRNGEO_1", "IRNGEO_2", "IRNGEO_3", "Теоретическое значение"]
        matExpec1 = commonFunc.getMathematicalExpectation(list1, len(list1))
        dispersion1 = commonFunc.getDispersion(list1, len(list1), matExpec1)
        matExpec2 = commonFunc.getMathematicalExpectation(list2, len(list2))  # len(list2) - длина меньше n, мат ожидание неверное?
        dispersion2 = commonFunc.getDispersion(list2, len(list2), matExpec2)  # Дисперсия супер верная при len(list2) < n
        matExpec3 = commonFunc.getMathematicalExpectation(list3, len(list3))
        dispersion3 = commonFunc.getDispersion(list3, len(list3), matExpec3)
        resultTable.add_row(["M = \n D = ", "%f\n%f" % (matExpec1, dispersion1), "%f\n%f" % (matExpec2, dispersion2), "%f\n%f" % (matExpec3, dispersion3), "%f\n%f" % (2, 2.2)])
        print(resultTable)


geometricDist1 = GeometricDist(10000, 0.5, "1")
geometricDist2 = GeometricDist(10000, 0.5, "2")
geometricDist3 = GeometricDist(10000, 0.5, "3")

geometricDist1.outputResult(geometricDist1.geomList, geometricDist2.geomList, geometricDist3.geomList)


