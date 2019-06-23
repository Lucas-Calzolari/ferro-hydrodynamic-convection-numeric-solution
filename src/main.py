import numpy as np
from parameter import L, H, WIDTH, HEIGHT, ERROR_TOLERANCE
import matrixProcessing
import utils
import math

isFlowStable = False
oldU = np.empty((WIDTH, HEIGHT))
newU = np.ones((WIDTH, HEIGHT))
matrixProcessing.setUBoundaries(newU)
matrixProcessing.setUBoundaries(oldU)

oldV = np.empty((WIDTH, HEIGHT))
newV = np.ones((WIDTH, HEIGHT))
matrixProcessing.setVBoundaries(newV)
matrixProcessing.setVBoundaries(oldV)

HX = np.empty((WIDTH, HEIGHT))
HY = np.empty((WIDTH, HEIGHT))

dU = np.empty((WIDTH, HEIGHT))

matrixProcessing.calculateHX(HX)
matrixProcessing.calculateHY(HY)

biggestVariation = math.inf
iterationNumber = 0

while biggestVariation > ERROR_TOLERANCE:
    aux = oldU
    oldU = newU
    newU = aux

    aux = oldV
    oldV = newV
    newV = aux

    matrixProcessing.calculateU(newU, oldU, oldV, HX, HY)
    matrixProcessing.calculateV(newV, oldU, oldV, HX, HY)

    biggestVariation = max( np.amax(np.absolute(newU-oldU)), np.amax(np.absolute(newV-oldV)) )
    iterationNumber += 1

    if (iterationNumber % 1000) == 0:
        print("i = ", iterationNumber)
        print("Current variation ", biggestVariation)


oldT = np.empty((WIDTH, HEIGHT))
newT = np.ones((WIDTH, HEIGHT))
matrixProcessing.setTBoundaries(newT)
matrixProcessing.setTBoundaries(oldT)

print("Start calculating T")
biggestVariation = math.inf
iterationNumber = 0
while biggestVariation > ERROR_TOLERANCE:

    aux = oldT
    oldT = newT
    newT = aux

    matrixProcessing.calculateT(newT, oldT, oldU, oldV, HX, HY)

    biggestVariation = np.amax(np.absolute(newT-oldT))
    iterationNumber += 1
    
    if (iterationNumber % 1000) == 0:
        print("i = ", iterationNumber)
        print("Current variation ", biggestVariation)



utils.printToFile("Final U\n")
utils.printArrayMirrored(newU)

utils.printToFile("Final V\n")
utils.printArrayMirrored(newV)

utils.printToFile("Final T\n")
utils.printArrayMirrored(newT)

utils.printToFile("HX\n")
utils.printArrayMirrored(HX)

utils.printToFile("HY\n")
utils.printArrayMirrored(HY)
