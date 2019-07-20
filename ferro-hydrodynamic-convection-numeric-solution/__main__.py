import numpy as np
# from .parameter import L, H, WIDTH, HEIGHT, ERROR_TOLERANCE, T_ERROR_TOLERANCE
# from . import matrixProcessing
import math
import sys
import os
from shutil import copyfile
from .cli_parser import get_arguments
from .parameter_utils import load_parameters
from .simulation import SimulationManager

if __name__ == "__main__":

    cli_args = get_arguments()

    simulation_manager = SimulationManager(params=cli_args.params_path)
    simulation_manager.startsimulation()
    # isFlowStable = False
    # oldU = np.empty((WIDTH, HEIGHT))
    # newU = np.ones((WIDTH, HEIGHT))
    # matrixProcessing.setUBoundaries(newU)
    # matrixProcessing.setUBoundaries(oldU)

    # oldV = np.empty((WIDTH, HEIGHT))
    # newV = np.ones((WIDTH, HEIGHT))
    # matrixProcessing.setVBoundaries(newV)
    # matrixProcessing.setVBoundaries(oldV)

    # HX = np.empty((WIDTH, HEIGHT))
    # HY = np.empty((WIDTH, HEIGHT))

    # dU = np.empty((WIDTH, HEIGHT))

    # matrixProcessing.calculateHX(HX)
    # matrixProcessing.calculateHY(HY)

    # biggestVariation = math.inf
    # iterationNumber = 0

    # while biggestVariation > ERROR_TOLERANCE and iterationNumber < 200:
    #     aux = oldU
    #     oldU = newU
    #     newU = aux

    #     aux = oldV
    #     oldV = newV
    #     newV = aux

    #     matrixProcessing.calculateU(newU, oldU, oldV, HX, HY)
    #     matrixProcessing.calculateV(newV, oldU, oldV, HX, HY)

    #     biggestVariation = max( np.amax(np.absolute(newU-oldU)), np.amax(np.absolute(newV-oldV)) )
    #     iterationNumber += 1

    #     if (iterationNumber % 1000) == 0:
    #         print("i = ", iterationNumber)
    #         print("Current variation ", biggestVariation)


    # outputPath = "../build/" + simulationName + "/"
    # os.makedirs(outputPath)
    # np.savetxt( outputPath+ "U.csv", newU)
    # np.savetxt( outputPath+ "V.csv", newV)
    # copyfile("./parameter.py", outputPath+ "parameter.py")

    # oldT = np.empty((WIDTH, HEIGHT))
    # newT = np.ones((WIDTH, HEIGHT))
    # matrixProcessing.setTBoundaries(newT)
    # matrixProcessing.setTBoundaries(oldT)
    

    # print("Start calculating T")
    # biggestVariation = math.inf
    # iterationNumber = 0
    # while biggestVariation > T_ERROR_TOLERANCE and iterationNumber < 200:

    #     aux = oldT
    #     oldT = newT
    #     newT = aux

    #     matrixProcessing.calculateT(newT, oldT, oldU, oldV, HX, HY)

    #     biggestVariation = np.amax(np.absolute(newT-oldT))
    #     iterationNumber += 1
        
    #     if (iterationNumber % 1000) == 0:
    #         print("i = ", iterationNumber)
    #         print("Current variation ", biggestVariation)


    # np.savetxt( outputPath+ "T.csv", newT)
