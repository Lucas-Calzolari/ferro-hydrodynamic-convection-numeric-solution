import sys
import math
import matplotlib.pyplot as plt
import numpy as np

def plotProfilesComparison(A, B, path=None):
  relativeProfiles = [1/5, 1/2, 4/5]
  xProfiles = [math.floor(A.shape[0]*rp) for rp in relativeProfiles]
  for i, fixed_X  in enumerate(xProfiles):
    percentage = str(math.floor(relativeProfiles[i]*100))
    xA = A[fixed_X,:-1]
    yA = np.linspace(0, 100, A.shape[1]-1)

    xB = B[fixed_X,:-1]
    yB = np.linspace(0, 100, B.shape[1]-1)

    fig, ax = plt.subplots()  

    ax.plot(xA, yA, label='A')
    ax.plot(xB, yB, label='B')

    ax.legend()

    if path is None:
      plt.show()
    else:
      plt.savefig(path+percentage)

def plotProfiles(A, path=None):
  relativeProfiles = [1/5, 1/2, 4/5]
  xProfiles = [math.floor(A.shape[0]*rp) for rp in relativeProfiles]
  for i, fixed_X  in enumerate(xProfiles):

    percentage = str(math.floor(relativeProfiles[i]*100))
    x = A[fixed_X,:-1]
    y = np.linspace(0, 100, A.shape[1]-1)

    fig, ax = plt.subplots()  
    ax.plot(x, y, label='Profile ')

    plt.hlines(y, np.zeros(y.shape[0]), x)
    if path is None:
      plt.show()
    else:
      plt.savefig(path+"_X_"+percentage)

  yProfiles = [math.floor(A.shape[1]*rp) for rp in relativeProfiles]
  for i, fixed_Y  in enumerate(yProfiles):

    percentage = str(math.floor(relativeProfiles[i]*100))
    y = A[:,fixed_Y]
    x = np.linspace(0, 100, A.shape[0])

    fig, ax = plt.subplots()  
    ax.plot(x, y, label='Profile ')

    # plt.hlines(y, np.zeros(y.shape[0]), x)
    if path is None:
      plt.show()
    else:
      plt.savefig(path+"_Y_"+percentage)
  
if __name__ == "__main__":
    if len(sys.argv) == 1:
        print("Usage: python main.py SIMULATION_NAME")
        exit()

    simulationName = sys.argv[1]

    outputPath = "../build/" + simulationName + "/"

    U = np.genfromtxt(outputPath + "U.csv")
    V = np.genfromtxt(outputPath + "V.csv")
    T = np.genfromtxt(outputPath + "T.csv")

    plotProfiles(U, path=outputPath+"U_PROFILE")
    plotProfiles(V, path=outputPath+"V_PROFILE")
    plotProfiles(T, path=outputPath+"T_PROFILE")

    if(len(sys.argv) > 2):
      comparisionName = sys.argv[2]

      outputPathB = "../build/" + comparisionName + "/"
      UB = np.genfromtxt(outputPathB + "U.csv")
      VB = np.genfromtxt(outputPathB + "V.csv")
      TB = np.genfromtxt(outputPathB + "T.csv")

      plotProfilesComparison(U,UB, path=outputPath+"COMPARISION_" + comparisionName+"_U_")
      plotProfilesComparison(V,VB, path=outputPath+"COMPARISION_" + comparisionName+"_V_")
      plotProfilesComparison(T,TB, path=outputPath+"COMPARISION_" + comparisionName+"_T_")

