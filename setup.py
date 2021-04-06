# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 13:12:55 2020

@author: María Pedrosa Bustos (mpedrosab@gmail.com)
"""

from cx_Freeze import setup, Executable

base = None    

executables = [Executable("FFT.py", base=base)]

packages = ["idna"]
options = {
    'build_exe': {    
        'packages':packages,
    },    
}

setup(
    name = "<any name>",
    options = options,
    version = "<any number>",
    description = '<any description>',
    executables = executables
)