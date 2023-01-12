# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for RockPi S board
(see https://wiki.radxa.com/RockpiS/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpis_v12
   from OPi import GPIO

   GPIO.setmode(radxa.rockpis_v12.BOARD)
"""

# Rock Pi S Hardware V12 physical board pin to GPIO pin
BOARD = {
    3:     11,   
    5:     12,
    7:     68,
    11:    15,
    13:    16,
    15:    17, 
    19:    55,
    21:    54,
    23:    56,
    43:    76,
    45:    72,
    8:     65,   
    10:    64,
    12:    69,
    16:    74,
    18:    73,
    22:    71,
    24:    57,
    28:    77,
    30:    78,
    32:    79,
    34:    80,
    44:    75,
    46:    70,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
