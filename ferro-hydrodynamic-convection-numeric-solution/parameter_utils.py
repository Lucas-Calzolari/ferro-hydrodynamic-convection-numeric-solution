import json

MANDATORY_KEYS = {
    "L", "H", 
    "WIDTH", "HEIGHT", 
    "U0", "T0", "TS", "CHI", 
    "T_ERROR_TOLERANCE","ERROR_TOLERANCE","dt",
    "MAGNET_S","MAGNET_R","MAGNET_A","MAGNET_B","REYNOLDS","MAGNETIC_REYNOLDS","PRANDLT","MAGNETIC_ECKERT"}

def validate_parameters(parameters):
    parameter_keys = set(parameters.keys())

    if not MANDATORY_KEYS <= parameter_keys:
        missing_keys = MANDATORY_KEYS - parameter_keys
        error_message = "The following keys are missing on your parameters file.\n"
        error_message += ', '.join(missing_keys)  
        return error_message
    

def load_parameters(path):
    with open(path) as parameter_file:
        parameters = json.loads(parameter_file.read())
    validation_error = validate_parameters(parameters)
    if validation_error:
        raise Exception(validation_error)

    L, H, WIDTH, HEIGHT = parameters["L"], parameters["H"], parameters["WIDTH"], parameters["HEIGHT"] 
    dx = L/(WIDTH-1)
    dy = H/(HEIGHT-1)
    parameters["dx"] = dx
    parameters["dy"] = dy

    return parameters