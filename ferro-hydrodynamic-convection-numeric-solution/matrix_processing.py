import numpy as np
from . import equations

class SerialMeshProcessor:
    def __init__(self, params):
        self.WIDTH = params["WIDTH"]
        self.HEIGHT = params["HEIGHT"]

        self.BOUNDARY_U_TOP = params["U0"]
        self.BOUNDARY_U_BOTTOM = 0
        self.BOUNDARY_U_LEFT = params["U0"]

        self.BOUNDARY_V_TOP = 0
        self.BOUNDARY_V_BOTTOM = 0
        self.BOUNDARY_V_LEFT = 0

        self.BOUNDARY_T_TOP = params["T0"]
        self.BOUNDARY_T_BOTTOM = params["TS"]
        self.BOUNDARY_T_LEFT = params["T0"]

        self.params = params


    def set_u_boundaries(self, U):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        BOUNDARY_U_TOP, BOUNDARY_U_BOTTOM, BOUNDARY_U_LEFT = self.BOUNDARY_U_TOP, self.BOUNDARY_U_BOTTOM, self.BOUNDARY_U_LEFT 

        U[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_U_TOP)
        U[0] = np.full(HEIGHT, BOUNDARY_U_LEFT)
        U[:, 0] = np.full(WIDTH, BOUNDARY_U_BOTTOM)

    def set_v_boundaries(self, V):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        BOUNDARY_V_TOP, BOUNDARY_V_BOTTOM, BOUNDARY_V_LEFT = self.BOUNDARY_V_TOP, self.BOUNDARY_V_BOTTOM, self.BOUNDARY_V_LEFT 

        V[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_V_TOP)
        V[0] = np.full(HEIGHT, BOUNDARY_V_LEFT)
        V[:, 0] = np.full(WIDTH, BOUNDARY_V_BOTTOM)

    def set_t_boundaries(self, T):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        BOUNDARY_T_TOP, BOUNDARY_T_BOTTOM, BOUNDARY_T_LEFT = self.BOUNDARY_T_TOP, self.BOUNDARY_T_BOTTOM, self.BOUNDARY_T_LEFT 

        T[:,HEIGHT-1] = np.full(WIDTH, BOUNDARY_T_TOP)
        T[0] = np.full(HEIGHT, BOUNDARY_T_LEFT)
        T[:, 0] = np.full(WIDTH, BOUNDARY_T_BOTTOM)


    def calculate_hx(self, HX):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        for i in range(0, WIDTH):
            for j in range(0, HEIGHT):
                HX[i,j] = equations.calculate_hx_item(params,i,j)

    def calculate_hy(self, HY):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        for i in range(0, WIDTH):
            for j in range(0, HEIGHT):
                HY[i,j] = equations.calculate_hy_item(params, i,j)

    def calculate_u(self, U, oldU, oldV, HX, HY):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT-1):
                U[i,j] = equations.calculate_u_item(params, i,j,oldU,oldV, HX, HY)

        for j in range(1, HEIGHT-1):
                U[WIDTH-1, j] = U[WIDTH-2, j]

    def calculate_v(self, V, oldU, oldV, HX, HY):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT-1):
                V[i,j] = equations.calculate_v_item(params, i,j,oldU,oldV, HX, HY)

        for j in range(1, HEIGHT-1):
                V[WIDTH-1, j] = V[WIDTH-2, j]

    def calculate_t(self, T, oldT, oldU, oldV, HX, HY):
        params = self.params
        WIDTH, HEIGHT = params["HEIGHT"], params["WIDTH"]
        for i in range(1, WIDTH-1):
            for j in range(1, HEIGHT-1):
                T[i,j] = equations.calculate_t_item(params, i,j,oldU,oldV, oldT, HX, HY)

        for j in range(1, HEIGHT-1):
                T[WIDTH-1, j] = T[WIDTH-2, j]