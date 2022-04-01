"""path_config.py - gets current working directory path and sets global variables"""

import os
from sys import exit as sys_exit


def get_path() -> str:
    """Returns current working directory path"""
    current_path = os.getcwd()
    data_path = os.path.join(current_path, 'data')
    if os.path.isdir(data_path):
        return data_path

    os.mkdir(data_path)
    if not os.path.isdir(data_path):
        print("Could not create directory")
        sys_exit()
    return data_path


DATA_PATH = get_path()

RES_1366 = os.path.join(DATA_PATH, '1366x768')
RES_1980 = os.path.join(DATA_PATH, '1920x1080')
ARDOUGE_ASSETS = os.path.join(DATA_PATH, 'ardouge_assets')
BLOODS_ASSETS = os.path.join(DATA_PATH, 'bloods_assets')
CONSTRUCTION_ASSETS = os.path.join(DATA_PATH, 'construction_assets')
COOKER_ASSETS = os.path.join(DATA_PATH, 'cooker_assets')
INC = os.path.join(DATA_PATH, 'inc')
POLLIVNEACH_ASSETS = os.path.join(DATA_PATH, 'pollivneach_assets')
RUNECRAFTING_ASSETS = os.path.join(DATA_PATH, 'runecrafting_assets')
SEERS_ASSETS = os.path.join(DATA_PATH, 'seers_assets')
SMITHING_ASSETS = os.path.join(DATA_PATH, 'smithing_assets')
WINES_ASSETS = os.path.join(DATA_PATH, 'wines_assets')
WOODCUTTER_ASSETS = os.path.join(DATA_PATH, 'woodcutter_assets')
CONFIG = os.path.join(DATA_PATH, 'config.json')
