from pathlib import Path

from .garpos_v102.garpos_main import drive_garpos

for path in Path(__file__).parent.rglob('*'):
    if path.is_dir() and path.name == 'f90lib':
        print(path)
        LIB_DIRECTORY = str(path)

LIB_RAYTRACE = 'lib_raytrace.so'