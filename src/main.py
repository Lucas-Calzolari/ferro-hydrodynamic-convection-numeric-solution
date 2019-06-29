import numpy as np
from parameter import L, H, WIDTH, HEIGHT, ERROR_TOLERANCE, T_ERROR_TOLERANCE
import matrixProcessing
import math
import sys
import os
from shutil import copyfile

if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python main.py SIMULATION_NAME")
        exit()

    simulationName = sys.argv[1]

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

    while biggestVariation > ERROR_TOLERANCE and iterationNumber < 200000:
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


    outputPath = "../build/" + simulationName + "/"
    os.makedirs(outputPath)
    np.savetxt( outputPath+ "U.csv", newU)
    np.savetxt( outputPath+ "V.csv", newV)
    copyfile("./parameter.py", outputPath+ "parameter.py")

    oldT = np.empty((WIDTH, HEIGHT))
    newT = np.ones((WIDTH, HEIGHT))
    matrixProcessing.setTBoundaries(newT)
    matrixProcessing.setTBoundaries(oldT)
    

    print("Start calculating T")
    biggestVariation = math.inf
    iterationNumber = 0
    while biggestVariation > T_ERROR_TOLERANCE and iterationNumber < 200000:

        aux = oldT
        oldT = newT
        newT = aux

        matrixProcessing.calculateT(newT, oldT, oldU, oldV, HX, HY)

        biggestVariation = np.amax(np.absolute(newT-oldT))
        iterationNumber += 1
        
        if (iterationNumber % 1000) == 0:
            print("i = ", iterationNumber)
            print("Current variation ", biggestVariation)


    np.savetxt( outputPath+ "T.csv", newT)

