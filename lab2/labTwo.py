from lab2 import binomialDist, dist, geometricDist, poissonDist, logarithmicDist


n = 10000

print("ДИСКРЕТНЫЕ РАСПРЕДЕЛЕНИЯ \n\n")
print("Выберите распределение (напечатайте нужную цифру):\n")

distChoice = input("1 - Равномерное распределение; \n 2 - Биномиальное распределение; \n 3 - Геометрическое распределение;"
      "\n 4 - Пуассоновское распределение; \n 5 - Логарифмическое распределение;\n\n")

if (distChoice == 1):
    dist = dist.UniformDist(n, 1, 100)
    print("Равномерное распределение:")
    dist.outputResult()
    dist.graphSimulationResult()
    dist.graphProbabilityDensity()
    dist.graphIntegralProbabilityDensity()
elif (distChoice == 2):
    dist1 = binomialDist.BinomialDist(n, 10, 0.5, "BNL")
    dist2 = binomialDist.BinomialDist(n, 10, 0.5, "BIN")
    print("Биномиальное распределение:")
    dist1.outputResult(dist1.binomList, dist2.binomList)
    dist1.graphSimulationResult()
    dist2.graphSimulationResult()
    dist1.graphProbabilityDensity()
    dist1.graphIntegralProbabilityDensity()
elif (distChoice == 3):
    dist1 = geometricDist.GeometricDist(n, 0.5, "1")
    dist2 = geometricDist.GeometricDist(n, 0.5, "2")
    dist3 = geometricDist.GeometricDist(n, 0.5, "3")
    print("Геометрическое распределение:")
    dist1.outputResult(dist1.geomList, dist2.geomList, dist3.geomList)
    dist1.graphSimulationResult()
    dist2.graphSimulationResult()
    dist3.graphSimulationResult()
    dist1.graphProbabilityDensity()
    dist1.graphIntegralProbabilityDensity()
elif (distChoice == 4):
    dist1 = poissonDist.PoissonDist(n, 10, "PSN")
    dist2 = poissonDist.PoissonDist(n, 10, "SPEC")
    print("Пуассоновское распределение:")
    dist1.outputResult(dist1.poissList, dist2.poissList)
    dist1.graphSimulationResult()
    dist2.graphSimulationResult()
    dist1.graphProbabilityDensity()
    dist1.graphIntegralProbabilityDensity()
elif (distChoice == 5):
    dist = logarithmicDist.LogarithmicDist(n, 0.5)
    print("Логарифмическое распределение:")
    dist.outputResult()
    dist.graphSimulationResult()
    dist.graphProbabilityDensity()
    dist.graphIntegralProbabilityDensity()
