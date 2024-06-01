# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa Zero3
(see https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface)

Usage:

.. code:: python
   import radxa.zero
   from OPi import GPIO

   GPIO.setmode(radxa.zero.BOARD) or GPIO.setmode(radxa.zero.BCM)
"""

# Amlogic S905Y2 GPIOs are grouped in two banks, GPIO AO domain and GPIO EE domain
#     AO domain: GPIOAO_0 - GPIOAO_11
#     EE domain: GPIOA_14 - GPIOA_15 | GPIOH_0 - GPIOH_8 | GPIOX_0 - GPIOX_19

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

# Radxa Zero physical board pin to GPIO pin
#https://docs.radxa.com/en/zero/zero3/hardware-design/hardware-interface
BOARD = {
   3:      32,     # GPIO1_A0 | UART3_RX_M0 | I2C3_SDA_M0
    5:      33,     # GPIO1_A1 | UART3_TX_M0 | I2C3_SCL_M0
    7:      116,    # GPIO3_C4 | PWM14_M0
    11:     97,     # GPIO3_A1
    13:     98,     # GPIO3_A2 | I2S3_MCLK_M0
    15:     104,    # GPIO3_B0
    19:     147,    # GPIO4_C3 | SPI3_MOSI_M1 | I2S3_SCLK_M1 | PWM15_IR_M1
    21:     149,    # GPIO4_C5 | SPI3_MISO_M1 | I2S3_SDO_M1 | PWM12_M1 | UART9_TX_M1
    23:     146,    # GPIO4_C2 | SPI3_CLK_M1 | I2S3_MCLK_M1 | PWM14_M1
    27:     138,    # GPIO4_B2 | I2S2_SDI_M1 | I2C4_SDA_M0
    29:     107,    # GPIO3_B3
    31:     108,    # GPIO3_B4
    33:     115,    # GPIO3_C3 | I2S1_SCLK_RX_M2 | UART5_RX_M1
    35:     100,    # GPIO3_A4 | I2S3_LRCK_M0
    37:     36,     # GPIO1_A4 | I2S1_SCLK_RX_M0
    8:      25,     # GPIO0_D1 | UART2_TX_M0
    10:     24,     # GPIO0_D0 | UART2_RX_M0
    12:     99,     # GPIO3_A3 | I2S3_SCLK_M0
    16:     105,    # GPIO3_B1 | UART4_RX_M1 | PWM8_M0
    18:     106,    # GPIO3_B2 | UART4_TX_M1 | PWM9_M0
    22:     113,    # GPIO3_C1 | I2S1_SDO2_M2
    24:     150,    # GPIO4_C6 | I2S3_SDI_M1 | UART9_RX_M1 | PWM13_M1 | SPI3_CS0_M1
    28:     139,    # GPIO4_B3 | I2S2_SDO_M1 | I2C4_SCL_M0
    32:     114,    # GPIO3_C2 | I2S1_SDO3_M2 | UART5_TX_M1
    36:     103,    # GPIO3_A7
    38:     102,    # GPIO3_A6 | I2S3_SDI_M0
    40:     101,    # GPIO3_A5 | I2S3_SDO_M0
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
