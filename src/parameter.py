L = 1
H = 3

# n represents the number of nodes, not divisions
WIDTH = 40
HEIGHT = 20

U0 = 1
T0 = 300
TS = 450

MI0 = 1

J = 2

CHI = 1

T_ERROR_TOLERANCE = 0.003
ERROR_TOLERANCE = 0.00001

dt = 0.000005

#Magnet dimensions
MAGNET_S = 2
MAGNET_R = 2
MAGNET_A = 0.8
MAGNET_B = 0.8

# Adimensional constants
REYNOLDS = 50
MAGNETIC_REYNOLDS = 1
PRANDLT = 1
MAGNETIC_ECKERT = 0.02

if (MAGNET_B > MAGNET_S):
    print("MAGNET_S SHOULD BE BIGGER THAN B")
    exit()