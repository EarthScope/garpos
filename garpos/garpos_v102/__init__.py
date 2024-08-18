from pathlib import Path
from .garpos_main import drive_garpos
LIB_DIRECTORY = Path(__file__).parent / "f90lib"
LIB_RAYTRACE = 'lib_raytrace.so'

from .f90lib import *