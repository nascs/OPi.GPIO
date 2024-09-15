# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock4
(see https://wiki.radxa.com/Rock3/hardware/3b/gpio)

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
    1:      12,   
    2:      114,
    3:      115,
    4:      112,
    6:      33,
    7:      32,
    8:      97,
    9:      113,
    10:     11,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
