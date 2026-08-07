import os
import subprocess

def clean_screen():
    if os.name == 'nt':
        subprocess.run('cls', shell = True)
    else:
        subprocess.run('clear', shell = True)