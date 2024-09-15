# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for RockPi S board
(see https://wiki.radxa.com/RockpiS/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpis_v11
   from OPi import GPIO

   GPIO.setmode(radxa.rockpis_v11.BOARD)
"""

# Rock Pi S Hardware V11 physical board pin to GPIO pin
BOARD = {
    3:      11,  
    5:      12,
    7:      69,
    11:     15,
    13:     16,
    15:     17,
    19:     55,
    21:     54,
    23:     56,   
    8:      65,  
    10:     64,
    12:     66,
    16:     67,
    18:     73,
    22:     14,
    24:     57,
    28:     70,
    30:     77,
    32:     78,
    34:     79,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
