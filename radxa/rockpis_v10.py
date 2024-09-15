# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for RockPi S board
(see https://wiki.radxa.com/RockpiS/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpis_v10
   from OPi import GPIO

   GPIO.setmode(radxa.rockpis_v10.BOARD)
"""

# Rock Pi S Hardware V10 physical board pin to GPIO pin
BOARD = {
    3:      12,   
    5:      11,
    7:      69,
    9:      64,
    11:     65,
    13:     66,
    15:     67,
    19:     55,
    21:     54,
    23:     56,
    8:      155,
    10:     154,
    12:     16,
    16:     71,
    18:     73,
    22:     14,
    24:     57,
    26:     15,
    28:     70,
    30:     77,
    32:     78,
    34:     79,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
