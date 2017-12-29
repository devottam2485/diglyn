import os
import posixpath
import sys
import base64
import platform

python = 2
if sys.version_info[0] > 2:
    python = 3

root_path = os.path.dirname(__file__)

class DLLocation(object):

    def __init__(self, name=None):

        if not name:
            self.get_DL_local()
        else:
            raise ValueError("Specific locations not currently supported.")

    def get_DL_local(self):

        DL_loc_path = posixpath.join(root_path, 'DL_Location.ini')

        with open(DL_loc_path) as infile:
            contents = infile.read()

        if python == 2:
            defaults = base64.decodestring(contents)
        else:
            defaults = base64.decodebytes(bytes(contents, 'ascii'))
            defaults = defaults.decode('ascii')

        setattr(self, 'location', defaults)