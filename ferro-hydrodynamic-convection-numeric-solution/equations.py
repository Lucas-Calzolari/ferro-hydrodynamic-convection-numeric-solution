import numpy as np
import math



def calculate_hx_item(params, i,j):
    dx, dy, S, R, A, B, K = params["dx"], params["dy"], params["MAGNET_S"], params["MAGNET_R"], params["MAGNET_A"], params["MAGNET_B"], params["K"]

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

def calculate_hy_item(params, i,j):
    dx, dy, S, R, A, B, K = params["dx"], params["dy"], params["MAGNET_S"], params["MAGNET_R"], params["MAGNET_A"], params["MAGNET_B"], params["K"]
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

def calculate_u_item(params, i,j, U, V, HX, HY):
    dx, dy, dt, REYNOLDS, CHI, MAGNETIC_REYNOLDS = params["dx"], params["dy"], params["dt"], params["REYNOLDS"], params["CHI"], params["MAGNETIC_REYNOLDS"]
    reynoldsTerm = ( (U[i+1,j] - 2*U[i,j] + U[i-1,j]) /(dx**2) + (U[i,j+1] - 2*U[i,j] +U[i,j-1])/(dy**2) ) / REYNOLDS
    magneticReynoldsTerm = (HX[i,j] * (HX[i+1,j] - HX[i-1,j])/(2*dx) + HY[i,j] * (HX[i,j+1] - HX[i,j-1])/(2*dy)) * CHI/MAGNETIC_REYNOLDS
    previousTerm = U[i,j] * ( U[i+1,j] - U[i-1,j] )/(2*dx) + V[i,j] * ( U[i,j+1] - U[i,j-1])/(2*dy)

    dU = reynoldsTerm + magneticReynoldsTerm - previousTerm

    return U[i,j] + dt*dU

def calculate_v_item(params, i,j, U, V, HX, HY):
    dx, dy, dt, REYNOLDS, CHI, MAGNETIC_REYNOLDS = params["dx"], params["dy"], params["dt"], params["REYNOLDS"], params["CHI"], params["MAGNETIC_REYNOLDS"]
    reynoldsTerm = ( (V[i+1,j] - 2*V[i,j] + V[i-1,j]) /(dx**2) + (V[i,j+1] - 2*V[i,j] +V[i,j-1])/(dy**2) ) / REYNOLDS
    magneticReynoldsTerm = (HX[i,j] * (HY[i+1,j] - HY[i-1,j])/(2*dx) + HY[i,j] * (HY[i,j+1] - HY[i,j-1])/(2*dy)) * CHI/MAGNETIC_REYNOLDS
    previousTerm = U[i,j] * ( V[i+1,j] - V[i-1,j] )/(2*dx) + V[i,j] * ( V[i,j+1] - V[i,j-1])/(2*dy)

    dV = reynoldsTerm + magneticReynoldsTerm - previousTerm

    return V[i,j] + dt*dV

def calculate_t_item(params, i,j, U, V, T, HX, HY):
    dx, dy, dt, REYNOLDS, CHI, MAGNETIC_REYNOLDS, PRANDLT = params["dx"], params["dy"], params["dt"], params["REYNOLDS"], params["CHI"], params["MAGNETIC_REYNOLDS"], params["PRANDLT"]
    reynoldsTerm = (((T[i+1,j]-2*T[i,j]+T[i-1,j])/(dx**2))+((T[i,j+1]-2*T[i,j]+T[i,j-1])/(dy**2)))/(REYNOLDS*PRANDLT)
    magneticTerm = (HX[i,j]**2 * ((U[i+1,j]-U[i-1,j])/(2*dx))+ HY[i,j]**2 * ((V[i,j+1]-V[i,j-1])/(2*dy))+HX[i,j]*HY[i,j]*((V[i+1,j]-V[i-1,j])/(2*dx)+(U[i,j+1]-U[i,j-1])/(2*dy)))* MAGNETIC_ECKERT*(1+CHI) 
    previousTerm = U[i,j]*((T[i+1,j]-T[i-1,j])/(2*dx)) + V[i,j]*((T[i,j+1] - T[i,j-1])/(2*dy))

    # print("reynoldsTerm ", reynoldsTerm)
    # print("magneticTerm ", magneticTerm)
    # print("previousTerm ", previousTerm)

    dT = reynoldsTerm + magneticTerm - previousTerm

    return T[i,j] + dt*dT 
