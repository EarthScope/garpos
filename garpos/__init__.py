from pathlib import Path

from .garpos_v102.garpos_main import drive_garpos

from .load_module import LIB_DIRECTORY
if not LIB_DIRECTORY:
    raise FileNotFoundError('Could not find the fortran library directory')
LIB_RAYTRACE = 'lib_raytrace.so'

