# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa RockpiE
(see https://wiki.radxa.com/RockpiE/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpie
   from OPi import GPIO

   GPIO.setmode(radxa.rockpie.BOARD) or GPIO.setmode(radxa.zero.BCM)
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
    3:      68,  
    5:      69,
    7:      100,
    11:     96,
    13:     104,
    15:     98,
    19:     27,
    21:     83,
    23:     60,
    27:     97,
    29:     80,
    31:     79,
    33:     82,
    37:     66,
    8:      64,
    10:     65,
    12:     90,  
    22:     76,
    24:     67,
    26:     87,
    28:     81,
    32:     102,
    36:     85,
    38:     84,
    40:     86,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
