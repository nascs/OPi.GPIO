# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock4
(see https://wiki.radxa.com/Rock3/hardware/3b/gpio)

Usage:

.. code:: python
   import radxa.rock3b
   from OPi import GPIO

   GPIO.setmode(radxa.rock3b.BOARD) or GPIO.setmode(radxa.rock3b.BCM)
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


# Radxa rock3b physical board pin to GPIO pin
BOARD = {
    3:      32,   
    5:      33,
    7:      116,
    11:     97,
    13:     98,
    15:     104,
    19:     147,
    21:     149,
    23:     146,
    27:     138,
    29:     107,
    31:     108,
    33:     115,
    35:     100,
    37:     36,
    8:      25,
    10:     24,
    12:     99,
    16:     105,
    18:     106,
    22:     113,
    24:     150,
    26:     153,
    28:     139,
    32:     114,
    36:     103,
    38:     102,
    40:     101,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
