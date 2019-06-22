import numpy as np
import equations
import math
from parameter import U0, T0, TS, J, L, H, WIDTH, HEIGHT, MI0, MAGNET_A as A, MAGNET_B as B, MAGNET_R as R, MAGNET_S as S, REYNOLDS, MAGNETIC_REYNOLDS, CHI

BOUNDARY_U_TOP = U0
BOUNDARY_U_BOTTOM = 0
BOUNDARY_U_LEFT =  U0

BOUNDARY_V_TOP = 0
BOUNDARY_V_BOTTOM = 0
BOUNDARY_V_LEFT =  0

BOUNDARY_T_TOP = T0
BOUNDARY_T_BOTTOM = TS
BOUNDARY_T_LEFT =  T0

def setUBoundaries(U):
    U[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_U_TOP)
    U[0] = np.full(HEIGHT, BOUNDARY_U_LEFT)
    U[:, 0] = np.full(WIDTH, BOUNDARY_U_BOTTOM)

def setVBoundaries(V):
    V[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_V_TOP)
    V[0] = np.full(HEIGHT, BOUNDARY_V_LEFT)
    V[:, 0] = np.full(WIDTH, BOUNDARY_V_BOTTOM)

def setTBoundaries(T):
    T[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_T_TOP)
    T[0] = np.full(HEIGHT, BOUNDARY_T_LEFT)
    T[:, 0] = np.full(WIDTH, BOUNDARY_T_BOTTOM)


def calculateHX(HX):
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            HX[i,j] = equations.calculateHXItem(i,j)

def calculateHY(HY):
    for i in range(0, WIDTH):
        for j in range(0, HEIGHT):
            HY[i,j] = equations.calculateHYItem(i,j)

def calculateU(U, oldU, oldV, HX, HY):
    for i in range(1, WIDTH-1):
        for j in range(1, HEIGHT-1):
            U[i,j] = equations.calculateUItem(i,j,oldU,oldV, HX, HY)

    for j in range(1, HEIGHT-1):
        U[WIDTH-1, j] = U[WIDTH-2, j]

def calculateV(V, oldU, oldV, HX, HY):
    for i in range(1, WIDTH-1):
        for j in range(1, HEIGHT-1):
            V[i,j] = equations.calculateVItem(i,j,oldU,oldV, HX, HY)

    for j in range(1, HEIGHT-1):
        V[WIDTH-1, j] = V[WIDTH-2, j]

def calculateT(T, oldT, oldU, oldV, HX, HY):
    for i in range(1, WIDTH-1):
        for j in range(1, HEIGHT-1):
            T[i,j] = equations.calculateTItem(i,j,oldU,oldV, oldT, HX, HY)

    for j in range(1, HEIGHT-1):
        T[WIDTH-1, j] = T[WIDTH-2, j]