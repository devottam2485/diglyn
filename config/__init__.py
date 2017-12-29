import os
import json
from location import DLLocation

config_root_path = os.path.dirname(__file__)

class DigitalLoc(object):

    def __init__(self, digiloc=''):
        digiloc = digiloc.lower()

        if digiloc == '':
            digiloc = DLLocation().location  # this needs to be replaced once v:\location.ini is switched to plaintext.

        filepath = os.path.join(config_root_path, 'location', digiloc + '.json')

        conf_file = open(filepath, 'r')
        studio_config = json.load(conf_file)
        conf_file.close()

        for key, value in studio_config.items():
            setattr(self, key, value)

