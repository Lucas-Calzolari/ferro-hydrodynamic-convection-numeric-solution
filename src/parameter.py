L = 1
H = .4

# n represents the number of nodes, not divisions
WIDTH = 30
HEIGHT = 15

U0 = 1
T0 = 300
TS = 450



MI0 = 1

J = 2

CHI = 1

ERROR_TOLERANCE = 0.00001

dt = 0.000005

#Magnet dimensions
MAGNET_S = 5
MAGNET_R = 5
MAGNET_A = 0.4
MAGNET_B = 0.4

# Adimensional constants
REYNOLDS = 50
MAGNETIC_REYNOLDS = 1
PRANDLT = 1
MAGNETIC_ECKERT = 10

if (MAGNET_B > MAGNET_S):
    print("MAGNET_S SHOULD BE BIGGER THAN B")
    exit()