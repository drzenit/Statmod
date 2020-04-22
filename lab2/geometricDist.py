from math import log

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



a = GeometricDist(10000, 0.5, "3")

print(a.createGeomList())

