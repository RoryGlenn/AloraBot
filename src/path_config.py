import os


def get_path(log=False):
    current_path = os.getcwd()
    data_path = os.path.join(current_path, 'data')
    if os.path.isdir(data_path):
        return data_path
    else:
        os.mkdir(data_path)
        if os.path.isdir(data_path):
            return data_path


data_path = get_path()

res_1366 = os.path.join(data_path, '1366x768')
res_1980 = os.path.join(data_path, '1920x1080')
ardouge_assets = os.path.join(data_path, 'ardouge_assets')
bloods_assets = os.path.join(data_path, 'bloods_assets')
construction_assets = os.path.join(data_path, 'construction_assets')
cooker_assets = os.path.join(data_path, 'cooker_assets')
inc = os.path.join(data_path, 'inc')
pollivneach_assets = os.path.join(data_path, 'pollivneach_assets')
runecrafting_assets = os.path.join(data_path, 'runecrafting_assets')
seers_assets = os.path.join(data_path, 'seers_assets')
smithing_assets = os.path.join(data_path, 'smithing_assets')
wines_assets = os.path.join(data_path, 'wines_assets')
woodcutter_assets = os.path.join(data_path, 'woodcutter_assets')
config = os.path.join(data_path, 'config.json')
