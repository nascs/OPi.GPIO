# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock4
(see https://wiki.radxa.com/Rock3/CM3/IO/GPIO)

Usage:

.. code:: python
   import radxa.radxa_cm3_io
   from OPi import GPIO

   GPIO.setmode(radxa.radxa_cm3_io.BOARD) or GPIO.setmode(radxa.radxa_cm3_io.BCM)
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


# Radxa radxa_cm3_io physical board pin to GPIO pin
BOARD = {
    3:      13,   
    5:      14,
    7:      125,
    11:     23,
    13:     15,
    15:     19,
    19:     138,
    21:     136,
    23:     139,
    27:     140,
    29:     137,
    31:     21,
    33:     22,
    35:     135,
    37:     18,
    8:      25,
    10:     24,
    12:     119,
    16:     124,
    18:     123,
    22:     118,
    24:     134,
    28:     141,
    32:     144,
    36:     135,
    38:     122,
    40:     121,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
