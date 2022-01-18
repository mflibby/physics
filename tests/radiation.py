import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from physics.radiation.formulas import *
from physics.constants.constants import *

def main():
    st = 1.23e-6
    F = 1.6e-19
    print(brightness_temperature(100*10**6, F/st, CGS))



if __name__ == '__main__':
    main()