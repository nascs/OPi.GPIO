# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa RockpiX
(see https://wiki.radxa.com/RockpiX/hardware/gpio)

Usage:

.. code:: python
   import radxa.rockpix
   from OPi import GPIO

   GPIO.setmode(radxa.rockpix.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""

# ╔═════════════╦═════════════╦════════╦══════════╦═════════════════╗
# ║  GPIO Group ║  GPIO Name  ║  Base  ║  Offset  ║  Formula        ║
# ╠═════════════╬═════════════╬════════╬══════════╬═════════════════╣
# ║  Virtual    ║    N/A      ║  412   ║  0-11    ║  Base + Offset  ║
# ║  First      ║  GPIOE_x    ║  424   ║  0-2     ║  Base + Offset  ║
# ║  Second     ║  GPIOZ_x    ║  427   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOH_x    ║  443   ║  0-8     ║  Base + Offset  ║
# ║  Second     ║  BOOT_x     ║  452   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOC_x    ║  468   ║  0-7     ║  Base + Offset  ║
# ║  Second     ║  GPIOA_x    ║  476   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOX_x    ║  492   ║  0-19    ║  Base + Offset  ║
# ╚═════════════╩═════════════╩════════╩══════════╩═════════════════╝



# Radxa rockpix physical board pin to GPIO pin
BOARD = {
    7:      335,
    21:     334,
    29:     338,
    31:     329,
    37:     348,
    12:     342,  
    16:     346,
    24:     332,
    26:     336,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
