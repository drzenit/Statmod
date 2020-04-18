from lab2 import commonFunc


class BinomialDist():
    def __init__(self, n: int, N: int, p: float):
        self.n = n
        self.numbList = commonFunc.generateRandomList(self.n)
        self.N = N
        self.p = p
        for i in self.numbList:
            self.binomList = commonFunc.IRNUNI(0, self.N, i)

a = BinomialDist(1000, 10, 0.5)

print(a.binomList)