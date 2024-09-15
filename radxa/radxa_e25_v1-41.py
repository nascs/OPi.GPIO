# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa radxa_e25
(see https://wiki.radxa.com/Rock3/CM3p/e25/GPIO)

Usage:

.. code:: python
   import radxa.radxa_e25
   from OPi import GPIO

   GPIO.setmode(radxa.radxa_e25.BOARD) or GPIO.setmode(radxa.radxa_e25.BCM)
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


# Radxa radxa_e25 physical board pin to GPIO pin
BOARD = {
    3:      32,   
    5:      33,
    7:      111,
    11:     116,
    13:     117,
    15:     113,
    19:     89,
    21:     88,
    23:     91,
    8:      114,
    10:     115,
    12:     99,
    16:     90,
    18:     22,
    24:     150,
    26:     112,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
