from setuptools import setup,find_namespace_packages,Extension
from setuptools.command.install import install
import platform
from pathlib import Path
import subprocess

class CustomInstallCommand(install):

    def find_dir(self, base_path, dir_name):
        for path in base_path.rglob("*"):
            if path.is_dir() and path.name == dir_name:
                return path
        return None
    
    def run(self):
        install.run(self)
        # Define the target directory for cloning
        target_dir = Path(__file__).parent / "bin"
        fortran_source = self.find_dir(target_dir, "f90lib")
        build_command = "gfortran -shared -fPIC -fopenmp -O3 -o lib_raytrace.so sub_raytrace.f90 lib_raytrace.f90"
        subprocess.run(build_command.split(), cwd=fortran_source)

f90_extension = Extension(
    name="garpos.f90lib",
    sources=["garpos/garpos_v102/f90lib/*"],
)
setup(
    name="garpos",
    version="1.0.2",
    python_requires=">=3.7",
    packages=find_namespace_packages(),
    package_data={"garpos": ["garpos/garpos_v102/f90lib/*"]},
    install_requires=[
        "numpy",
        "scipy",
        "matplotlib",
        "pandas",
        "scikit-sparse",
    ],


    cmdclass={
        "install": CustomInstallCommand
    },
)
