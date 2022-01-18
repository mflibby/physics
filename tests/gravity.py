import os
import sys
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from physics.gravity.newtonian.formulas import *
from physics.constants.constants import *


print(gravitational_force( 75 , MASS_EARTH , 6371000))