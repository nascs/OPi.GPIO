# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock5C
(see https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface)

Usage:

.. code:: python
   import radxa.rock5c
   from OPi import GPIO

   GPIO.setmode(radxa.rock5c.BOARD) or GPIO.setmode(radxa.rock5c.BCM)
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
#https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface
BOARD = {
    3:      63,
    5:      62,
    7:      43,
    11:     139,
    13:     138,
    15:     140,
    19:     33,
    21:     32,
    23:     34,
    27:     23,
    29:     42,
    31:     41,
    33:     44,
    35:     128,
    8:      13,
    10:     14,
    12:     129,
    16:     37,
    18:     40,
    24:     45,
    26:     35,
    28:     36,
    32:     136,
    36:     130,
    38:     133,
    40:     137,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
