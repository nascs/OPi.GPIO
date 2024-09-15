# -*- coding: utf-8 -*-
# Copyright (c) 2018 Richard Hull & Contributors
# See LICENSE.md for details.

"""
Alternative pin mappings for Radxa rock5C and rock5A
(see https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface
     https://docs.radxa.com/en/rock5/rock5a/hardware-design/hardware-interface )

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
# ║  GPIO0      ║     0       ║      A      ║     0       ║  
# ╠═════════════╬═════════════╬═════════════╬═════════════╣	
# ║  GPIO1      ║     32      ║      B      ║     8       ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣		
# ║  GPIO2      ║     64      ║      C      ║     16      ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO3      ║     96      ║      D      ║     24      ║
# ╠═════════════╬═════════════╬═════════════╬═════════════╣
# ║  GPIO4      ║     128     ║             ║             ║
# ╚═════════════╩═════════════╩═════════════╩═════════════╝


# Radxa rock5C and rock5A physical board pin to GPIO pin
#https://docs.radxa.com/en/rock5/rock5c/hardware-design/hardware-interface
#https://docs.radxa.com/en/rock5/rock5a/hardware-design/hardware-interface
BOARD = {
 3:      63,     # GPIO1_D7 | UART1_CTSN_M1 | I2C8_SDA_M2 | PWM15_IR_M3
    5:      62,     # GPIO1_D6 | UART1_RTSN_M1 | I2C8_SCL_M2 | PWM14_M2
    7:      43,     # GPIO1_B3 | UART4_TX_M2
    11:     139,    # GPIO4_B3 | UART8_CTSN_M0 | I2C7_SDA_M3 | PWM15_IR_M1 | CAN1_TX_M1 | I2S1_SDO2_M0
    13:     138,    # GPIO4_B2 | UART8_RTSN_M0 | I2C7_SCL_M3 | PWM14_M1 | CAN1_RX_M1 | I2S1_SDO1_M0 | SPI0_CS0_M1
    15:     140,    # GPIO4_B4 | UART9_TX_M1 | PWM11_IR_M1 | SPDIF0_TX_M1 | I2S1_SDO3_M0
    19:     33,     # GPIO1_A1 | UART6_TX_M1 | I2C2_SCL_M4 | SPI4_MOSI_M2
    21:     32,     # GPIO1_A0 | UART6_RX_M1 | I2C2_SDA_M4 | SPI4_MISO_M2
    23:     34,     # GPIO1_A2 | UART6_RTSN_M1 | I2C4_SDA_M3 | PWM0_M2 | SPI4_CLK_M2
    27:     23,     # GPIO0_C7 | UART1_RTSN_M2 | I2C6_SDA_M0 | PWM6_M0 | I2S1_SDI2_M1 | SPI0_MISO_M0
    29:     42,     # GPIO1_B2 | UART4_RX_M2 | SPI0_MOSI_M2
    31:     41,     # GPIO1_B1 | SPI0_MISO_M2
    33:     44,     # GPIO1_B4 | UART7_RX_M2 | SPI0_CS0_M2
    35:     128,    # GPIO4_A0 | UART9_RTSN_M1 | I2S1_MCLK_M0 | SPI0_MISO_M1
    8:      13,     # GPIO0_B5 | UART2_TX_M0 | I2C1_SCL_M0 | I2S1_MCLK_M1
    10:     14,     # GPIO0_B6 | UART2_RX_M0 | I2C1_SDA_M0 | I2S1_SCLK_M1
    12:     129,    # GPIO4_A1 | UART9_CTSN_M1 | I2S1_SCLK_M0 | SPI0_MOSI_M1
    16:     37,     # GPIO1_A5 | SPI2_MOSI_M0
    18:     40,     # GPIO1_B0 | SPI2_CS1_M0
    22:     45,     # GPIO1_B5 | UART7_TX_M2 | SPI0_CS1_M2
    24:     35,     # GPIO1_A3 | UART6_CTSN_M1 | I2C4_SCL_M3 | PWM1_M2 | SPI4_CS0_M2
    26:     36,     # GPIO1_A4 | SPI2_MISO_M0
    28:     24,     # GPIO0_D0 | UART1_CTSN_M2 | I2C6_SCL_M0 | PWM7_IR_M0 | I2S1_SDI3_M1 | SPI3_MISO_M2
    30:     31,     # GPIO4_B0 | UART8_TX_M0 | I2C6_SDA_M3 | I2S1_SDI3_M0 | SPI2_CS1_M1
    32:     136,    # GPIO4_B0 | UART8_TX_M0 | I2C6_SDA_M3 | I2S1_SDI3_M0 | SPI2_CS1_M1
    34:     130,    # GPIO4_A2 | I2S1_LRCK_M0 | SPI0_CLK_M1
    38:     133,    # GPIO4_A5 | UART3_TX_M2 | I2C3_SDA_M2 | I2S1_SDI0_M0
    40:     137,    # GPIO4_B1 | UART8_RX_M0 | I2C6_SCL_M3 | SPDIF1_TX_M1 | I2S1_SDO0_M0 | SPI0_CS1_M1
}
"""PWM PINs:
(Check https://dl.radxa.com/rock5/5c/docs/hw/v1100/radxa_rock_5c_schematic_v1100.pdf page 11/25 & 15/25)
PWM3_IR_M1 GPIO3_B2 = 3*32+(B=1)*8+2=106
PWMFan: 106
""""
# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
