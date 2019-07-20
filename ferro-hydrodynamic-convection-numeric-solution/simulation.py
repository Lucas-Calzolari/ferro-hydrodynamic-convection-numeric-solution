import numpy as np
import math
from .parameter_utils import validate_parameters, load_parameters
from .matrix_processing import SerialMeshProcessor

class SimulationManager:
    def __init__(self, params):
        if isinstance(params, str):
            params = load_parameters(params)

        validation_error = validate_parameters(params) 
        if not validation_error is None:
            raise Exception(validation_error)
        self.params = params
        self.serial_processor = SerialMeshProcessor(self.params) 

    def initialize_u(self):
        WIDTH, HEIGHT = self.params["HEIGHT"], self.params["WIDTH"]

        old_u = np.empty((WIDTH, HEIGHT))
        new_u = np.ones((WIDTH, HEIGHT))
        self.serial_processor.set_u_boundaries(new_u)
        self.serial_processor.set_u_boundaries(old_u)

        self.old_u, self.new_u = old_u, new_u

    def initialize_v(self):
        WIDTH, HEIGHT = self.params["HEIGHT"], self.params["WIDTH"]

        old_v = np.empty((WIDTH, HEIGHT))
        new_v = np.ones((WIDTH, HEIGHT))
        self.serial_processor.set_v_boundaries(new_v)
        self.serial_processor.set_v_boundaries(old_v)

        self.old_v, self.new_v = old_v, new_v

    def initialize_hx(self):
        WIDTH, HEIGHT = self.params["HEIGHT"], self.params["WIDTH"]
        hx = np.empty((WIDTH, HEIGHT))
        self.serial_processor.calculate_hx(hx)
    
        self.hx = hx

    def initialize_hy(self):
        WIDTH, HEIGHT = self.params["HEIGHT"], self.params["WIDTH"]
        hy = np.empty((WIDTH, HEIGHT))
        self.serial_processor.calculate_hy(hy)
    
        self.hy = hy

    def initialize(self):
        self.initialize_u()
        self.initialize_v()
        self.initialize_hx()
        self.initialize_hy()

    def startsimulation(self):
        ERROR_TOLERANCE = self.params["ERROR_TOLERANCE"]
        self.initialize()

        biggestVariation = math.inf
        iterationNumber = 0

        while biggestVariation > ERROR_TOLERANCE and iterationNumber < 200000:
            aux = self.old_u
            self.old_u = self.new_u
            self.new_u = aux

            aux = self.old_v
            self.old_v = self.new_v
            self.new_v = aux

            self.serial_processor.calculate_u(self.new_u, self.old_u, self.old_v, self.hx, self.hy)
            self.serial_processor.calculate_v(self.new_v, self.old_u, self.old_v, self.hx, self.hy)

            biggestVariation = max( np.amax(np.absolute(self.new_u-self.old_u)), np.amax(np.absolute(self.new_v-self.old_v)) )
            iterationNumber += 1

            if (iterationNumber % 1000) == 0:
                print("i = ", iterationNumber)
                print("Current variation ", biggestVariation)