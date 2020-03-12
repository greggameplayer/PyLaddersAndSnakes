from setuptools import setup, find_packages
import sys
import os
os.system("py -m pip install --upgrade pip setuptools")
os.system("py -m pip install -r requirements.txt")
from cx_Freeze import setup, Executable
build_exe_options = {"includes": ["pypresence", "simpleaudio"], "optimize": 2, 'include_files': [("resources", "resources")]}

base = None
if sys.platform == 'win32':
    base = 'Win32GUI'

executables = [
    Executable('PyLaddersAndSnakes/__init__.py', base=base, icon="resources/images/snakes-and-ladders.ico",
               targetName="PyLaddersAndSnakes")
]

setup(
    name="PyLaddersAndSnakes",
    version="0.9.1",
    packages=["PyLaddersAndSnakes"],
    description='A snakes and ladders game written in python 3',
    author='Gregoire Hage',
    author_email='gregoire.hage@epsi.fr',

    # Project uses reStructuredText, so ensure that the docutils get
    # installed or upgraded on the target machine
    install_requires=["pypresence", "cx_Freeze"],
    options={"build_exe": build_exe_options},
    executables=executables
)