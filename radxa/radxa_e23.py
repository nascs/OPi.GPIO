# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock4
(see https://wiki.radxa.com/Rock3/hardware/3b/gpio)

Usage:

.. code:: python
   import radxa.radxa_e23
   from OPi import GPIO

   GPIO.setmode(radxa.radxa_e23.BOARD) or GPIO.setmode(radxa.radxa_e23.BCM)
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


# Radxa radxa_e23 physical board pin to GPIO pin
BOARD = {
    3:      32,   
    5:      33,
    7:      21,
    11:     97,
    13:     20,
    15:     22,
    19:     138,
    21:     136,
    23:     139,
    27:     14,
    29:     113,
    31:     114,
    33:     15,
    35:     29,
    37:     30,
    8:      25,
    10:     24,
    12:     108,
    22:     86,
    24:     134,
    26:     135,
    28:     13,
    32:     19,
    36:     12,
    38:     17,
    40:     11,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
