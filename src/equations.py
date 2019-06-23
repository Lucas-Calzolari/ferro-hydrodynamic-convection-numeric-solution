import numpy as np
from parameter import dt, WIDTH, HEIGHT, U0, J, L, H, MI0, MAGNET_A as A, MAGNET_B as B, MAGNET_R as R, MAGNET_S as S,MAGNETIC_ECKERT, PRANDLT, REYNOLDS, MAGNETIC_REYNOLDS, CHI
import math

# K = J/(4*math.pi*MI0)
K = 1
dx = L/(WIDTH-1)
dy = H/(HEIGHT-1)

def calculateHXItem(i,j):
    X = dx*i
    Y = dy*j

    TA = Y + S + B
    TB = X - R - A
    TC = Y + S - B
    TD = X - R + A 

    firstTermNumerator = TA + (TA**2 + TB**2)**0.5
    firstTermDenominator = TC + (TC**2 + TB**2)**0.5
    firstTerm = firstTermNumerator/firstTermDenominator

    secondTermNumerator = TC + (TC**2 + TD**2)**0.5
    secondTermDenominator = -TC + (TC**2 + TD**2)**0.5
    secondTerm = secondTermNumerator/secondTermDenominator

    # print("firstTermNumerator ", firstTermNumerator)
    # print("firstTermDenominator ", firstTermDenominator)
    # print("firstTerm ", firstTerm)

    # print("secondTermNumerator ", secondTermNumerator)
    # print("secondTermDenominator ", secondTermDenominator)
    # print("secondTerm ", secondTerm)

    # print("TA ", TA)
    # print("TB ", TB)
    # print("TC ", TC)
    # print("TD ", TD)

    return K*math.log(firstTerm*secondTerm)

def calculateHYItem(i,j):
    X = dx*i
    Y = dy*j

    TA = Y + S + B
    TB = X - R - A
    TC = Y + S - B
    TD = X - R + A

    firstTermNumerator = TD + (TC**2 + TD**2)**0.5
    firstTermDenominator = TB + (TC**2 + TB**2)**0.5
    firstTerm = firstTermNumerator/firstTermDenominator

    secondTermNumerator = TB + (TA**2 + TD**2)**0.5
    secondTermDenominator = -TD + (TA**2 + TB**2)**0.5
    secondTerm = secondTermNumerator/secondTermDenominator

    return K*math.log(firstTerm*secondTerm)

def calculateUItem(i,j, U, V, HX, HY):
    reynoldsTerm = ( (U[i+1,j] - 2*U[i,j] + U[i-1,j]) /(dx**2) + (U[i,j+1] - 2*U[i,j] +U[i,j-1])/(dy**2) ) / REYNOLDS
    magneticReynoldsTerm = (HX[i,j] * (HX[i+1,j] - HX[i-1,j])/(2*dx) + HY[i,j] * (HX[i,j+1] - HX[i,j-1])/(2*dy)) * CHI/MAGNETIC_REYNOLDS
    previousTerm = U[i,j] * ( U[i+1,j] - U[i-1,j] )/(2*dx) + V[i,j] * ( U[i,j+1] - U[i,j-1])/(2*dy)

    dU = reynoldsTerm + magneticReynoldsTerm - previousTerm

    return U[i,j] + dt*dU

def calculateVItem(i,j, U, V, HX, HY):
    reynoldsTerm = ( (V[i+1,j] - 2*V[i,j] + V[i-1,j]) /(dx**2) + (V[i,j+1] - 2*V[i,j] +V[i,j-1])/(dy**2) ) / REYNOLDS
    magneticReynoldsTerm = (HX[i,j] * (HY[i+1,j] - HY[i-1,j])/(2*dx) + HY[i,j] * (HY[i,j+1] - HY[i,j-1])/(2*dy)) * CHI/MAGNETIC_REYNOLDS
    previousTerm = U[i,j] * ( V[i+1,j] - V[i-1,j] )/(2*dx) + V[i,j] * ( V[i,j+1] - V[i,j-1])/(2*dy)

    dV = reynoldsTerm + magneticReynoldsTerm - previousTerm

    return V[i,j] + dt*dV

def calculateTItem(i,j, U, V, T, HX, HY):
    reynoldsTerm = (((T[i+1,j]-2*T[i,j]+T[i-1,j])/(dx**2))+((T[i,j+1]-2*T[i,j]+T[i,j-1])/(dy**2)))/(REYNOLDS*PRANDLT)
    magneticTerm = (HX[i,j]**2 * ((U[i+1,j]-U[i-1,j])/(2*dx))+ HY[i,j]**2 * ((V[i,j+1]-V[i,j-1])/(2*dy))+HX[i,j]*HY[i,j]*((V[i+1,j]-V[i-1,j])/(2*dx)+(U[i,j+1]-U[i,j-1])/(2*dy)))* MAGNETIC_ECKERT*(1+CHI) 
    previousTerm = U[i,j]*((T[i+1,j]-T[i-1,j])/(2*dx)) + V[i,j]*((T[i,j+1] - T[i,j-1])/(2*dy))

    # print("reynoldsTerm ", reynoldsTerm)
    # print("magneticTerm ", magneticTerm)
    # print("previousTerm ", previousTerm)

    dT = reynoldsTerm + magneticTerm - previousTerm

    return T[i,j] + dt*dT 
