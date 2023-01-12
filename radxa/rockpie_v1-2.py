# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa RockpiE
(see https://wiki.radxa.com/RockpiE/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpie_v1-2
   from OPi import GPIO

   GPIO.setmode(radxa.rockpie_v1-2.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""

# formula: GPIO Bank + Base Num
# ╔═════════════╦═════════════╦═════════════╦═════════════╗
# ║  GPIO Bank  ║   Base Num  ║  GPIO Group ║   Base Num  ║        
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO0 		║     0		  ║     A		║     0       ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣	
# ║  GPIO1		║     32	  ║     B		║     8		  ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣		
# ║  GPIO2		║     64	  ║	    C   	║	 16       ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO3		║     96  	  ║	    D		║    24       ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO4		║    128      ║             ║             ║
# ╚═════════════╩═════════════╩═════════════╩═════════════╝

# Radxa rockpie physical board pin to GPIO pin
BOARD = {
    3:      100,
    5:      102,
    7:      60,
    11:     66,
    13:     67,
    15:     27,
    19:     97,
    21:     98,
    23:     96,
    27:     68,
    29:     84,
    31:     85,
    33:     70,
    35:     81,
    37:     86,
    8:      64,
    10:     65,
    12:     82,
    24:     104,
    26:     76,
    28:     69,
    32:     80,
    36:     79,
    38:     83,
    40:     87,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
