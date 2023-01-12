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
    7:      13,
    11:     116,
    13:     117,
    15:     16,
    19:     147,
    21:     149,
    23:     146,
    27:     12,
    29:     95,
    31:     96,
    33:     115,
    35:     100,
    8:      25,
    10:     24,
    12:     99,
    16:     14,
    18:     106,
    22:     17,
    24:     150,
    26:     153,
    28:     11,
    32:     14,
    36:     98,
    38:     102,
    40:     101,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
