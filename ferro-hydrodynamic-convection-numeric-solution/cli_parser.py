import argparse
import datetime
import os


DEFAULT_OUTPUT_PATH=os.getcwd()

def get_arguments():
    current_datetime = datetime.datetime.now().__str__()

    parser = argparse.ArgumentParser(description='Fluid simulation.')
    parser.add_argument('simulation_name', metavar='simulation name', type=str, nargs="?",
                        help='The simulation name, for clarity purposes. The output by default will use this name.',
                        default=current_datetime)
    parser.add_argument('-o', '--output-path',  type=str, nargs="?",
                        help='The output path where file will be created.',
                        default=DEFAULT_OUTPUT_PATH, dest="output_path")

    parser.add_argument('-p', '--params-path',  type=str, nargs="?",
                    help='The parameter file path (Format JSON expected).',
                    required=True, dest="params_path")

    parser.add_argument('--disable-temperature',  type=bool, nargs="?",
                        help='Flag to avoid temperature simulation.',
                        default=False, dest="disable_temperature")

    args = parser.parse_args()

    return args