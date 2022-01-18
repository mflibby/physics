from ...constants.constants import *


def gravitational_force(mass_1 : numeric, mass_2 : numeric, distance : numeric, unit_system : UnitSystem = SI) -> list[numeric, str]:
    return [unit_system.G_newt*mass_1*mass_2/distance**2, f"{unit_system.units.derived_names['force']}"]