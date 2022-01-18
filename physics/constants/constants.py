
from dataclasses import dataclass
from typing import *
from numpy import number 
from numbers import Number 


numeric = Union[Number, number]

c = 299_792_458 #m/s
K_BOLTZ = 0.000_000_000_000_000_000_000_013_806_49 # J/K
K_BOLTZ_EV = 0.000_086_173_332_621_45 #ev/K
K_BOLTZ_ERG = 0.000_000_000_000_000_138_064_9 # erg/K
G_NEWT = 0.0000000000667439 #m^3/kg s^2

MASS_EARTH = 5_972_000_000_000_000_000_000_000 # kg
MASS_SUN = 1_989_000_000_000_000_000_000_000_000_000 #kg
MASS_MOON = 73_476_730_900_000_000_000_000 #kg


class DerivedUnits(TypedDict):
    force : list[str, str]
    energy : list[str, str]
    power : list[str, str]
    pressure : list[str, str]

@dataclass
class Units:
    length : str
    mass : str
    time : str
    temperature : str
    derived_names : DerivedUnits
    def __post_init__ (self):
        self.velocity = f"{self.length}/{self.time}"
        self.acceleration = f"{self.length}/{self.time}^2"
        self.force = f"{self.mass} {self.length}/{self.time}^2"
        self.energy = f"{self.mass} {self.length}^2/{self.time}^2"
        self.power = f"{self.mass} {self.length}^2/{self.time}^3"
        self.pressure = f"{self.mass}/{self.length} {self.time}^2"

    

@dataclass
class UnitSystem:
    k_b : numeric # boltzmann's constant
    c : numeric # speed of light
    G_newt : numeric # Gravitational Constant ##May rename to G_grav

    units : Units



SI = UnitSystem( k_b = 0.000_000_000_000_000_000_000_013_806_49
               , c = 299_792_458
               , G_newt = 0.000_000_000_066_743_9
               , units = Units( 'm'
                              , 'kg'
                              , 's' 
                              , 'K'
                              , derived_names = { 'force' : ['N', 'Newton']
                                                , 'energy' : ['J', 'Joule']
                                                , 'power' : ['W', 'Watt']
                                                , 'pressure' : ['Pa', 'Pascal']
                                                }
                              )
               )

CGS = UnitSystem( k_b = 0.000_000_000_000_000_138_064_9 
                , c = 29_979_245_800
                , G_newt = 0.000_000_066_743_0 # dyn cm^2/g^2
                , units = Units( 'cm'
                               , 'g'
                               , 's' 
                               , 'K'
                               , derived_names = { 'force' : ['dyn', 'dyne']
                                                 , 'energy' : ['erg', 'erg']
                                                 , 'power' : ['erg/s', 'erg per second']
                                                 , 'pressure' : ['Ba', 'barye']
                                                 }
                               )
                )

