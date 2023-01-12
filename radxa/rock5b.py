# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock4
(see https://wiki.radxa.com/Rockpi4/hardware/gpio)

Usage:

.. code:: python
   import radxa.rock5B
   from OPi import GPIO

   GPIO.setmode(radxa.rock5B.BOARD) or GPIO.setmode(radxa.rock5B.BCM)
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


# Radxa rock5B physical board pin to GPIO pin
BOARD = {
    3:      71,
    5:      72,
    7:      75,
    11:     146,
    13:     150,
    15:     149,
    19:     40,
    21:     39,
    23:     41,
    27:     64,
    29:     74,
    31:     73,
    33:     76,
    35:     133,
    37:     158,
    8:      148,
    10:     147,
    12:     131,
    16:     154,
    18:     156,
    22:     157,
    24:     42,
    28:     65,
    32:     112,
    36:     132,
    38:     134,
    40:     135,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
