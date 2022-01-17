from ..constants.constants import *


def brightness_temperature(freq : float, I_freq, unit_system : UnitSystem = SI):
    """
        T_b = \frac{c^2}{2\nu**2k_b}*I_{\nu}
    """
    return (unit_system.c**2/(2*(freq**2)*unit_system.k_b))*I_freq
