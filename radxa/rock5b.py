# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock5B
(see https://docs.radxa.com/en/rock5/rock5b/hardware-design/hardware-interface)

Usage:

.. code:: python
   import radxa.rock5b
   from OPi import GPIO

   GPIO.setmode(radxa.rock5b.BOARD) or GPIO.setmode(radxa.rock5b.BCM)
"""

# formula: GPIO Bank + Base Num
# ╔═════════════╦═════════════╦═════════════╦═════════════╗
# ║  GPIO Bank  ║   Base Num  ║  GPIO Group ║   Base Num  ║        
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO0 		  ║     0		    ║     A		    ║     0       ║  
# ╠═════════════╬═════════════╬═════════════╬═════════════╣	
# ║  GPIO1		  ║     32	    ║     B	    	║     8  		  ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣		
# ║  GPIO2	  	║     64	    ║	    C     	║  	   16     ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO3		  ║     96  	  ║	    D	    	║      24     ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO4		  ║    128      ║             ║             ║
# ╚═════════════╩═════════════╩═════════════╩═════════════╝


# Radxa rock5C physical board pin to GPIO pin
#https://docs.radxa.com/en/rock5/rock5b/hardware-design/hardware-interface
BOARD = {
    3:      139,
    5:      138,
    7:      115,
    11:     113,
    13:     111,
    15:     112,
    19:     42,
    21:     41,
    23:     43,
    27:     150,
    29:     63,
    31:     47,
    33:     103,
    35:     110,
    8:      13,
    10:     14,
    12:     109,
    16:     100,
    18:     148,
    24:     44,
    26:     45,
    28:     114,
    32:     114,
    36:     105,
    38:     106,
    40:     107,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
