# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero2
(see https://wiki.radxa.com/Zero2/Hardware/GPIO)

Usage:

.. code:: python
   import radxa.zero2
   from OPi import GPIO

   GPIO.setmode(radxa.zero2.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""

# ╔═════════════╦═════════════╦════════╦══════════╦═════════════════╗
# ║  GPIO Chip  ║  GPIO Name  ║  Base  ║  Offset  ║  Formula        ║
# ╠═════════════╬═════════════╬════════╬══════════╬═════════════════╣
# ║  First      ║  GPIOAO_x   ║  412   ║  0-11    ║  Base + Offset  ║
# ║  First      ║  GPIOE_x    ║  424   ║  0-2     ║  Base + Offset  ║
# ║  Second     ║  GPIOZ_x    ║  427   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOH_x    ║  443   ║  0-8     ║  Base + Offset  ║
# ║  Second     ║  BOOT_x     ║  452   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOC_x    ║  468   ║  0-7     ║  Base + Offset  ║
# ║  Second     ║  GPIOA_x    ║  476   ║  0-15    ║  Base + Offset  ║
# ║  Second     ║  GPIOX_x    ║  492   ║  0-19    ║  Base + Offset  ║
# ╚═════════════╩═════════════╩════════╩══════════╩═════════════════╝

# Radxa Zero2 physical board pin to GPIO pin
BOARD = {
    3:      490,   
    5:      491,
    7:      429,
    11:     430,
    13:     430,
    15:     432,
    19:     447,
    21:     448,
    23:     450,
    27:     427,
    29:     419,
    31:     480,
    33:     420,
    35:     478,
    37:     421,
    8:      412,
    10:     413,
    12:     477,
    16:     435,
    18:     433,
    22:     436,
    24:     449,
    28:     428,
    32:     476,
    36:     479,
    38:     481,
    40:     434,
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
