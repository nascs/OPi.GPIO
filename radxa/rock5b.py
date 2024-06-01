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
    3:    139,    # GPIO4_B3  | CAN1_TX_M1  | PWM15_IR_M1  | UART8_CTSN_M0  | I2C7_SDA_M3  | I2S1_SDO2_M0
    5:    138,    # GPIO4_B2  | CAN1_RX_M1  | PWM14_M1  | UART8_RTSN_M0  | I2C7_SCL_M3  | I2S1_SDO1_M0
    7:    115,    # GPIO3_C3  | PWM15_IR_M0  | UART7_CTSN_M1  | I2C8_SDA_M4  | SPI1_CS1_M1
    11:   113,    # GPIO3_C1  | UART7_RX_M1  | SPI1_CLK_M1
    13:   111,    # GPIO3_B7  | I2C3_SCL_M1  | SPI1_MOSI_M1
    15:   112,    # GPIO3_C0  | UART7_TX_M1  | I2C3_SDA_M1  | SPI1_MISO_M1
    19:   42,     # GPIO1_B2  | UART4_RX_M2  | SPI0_MOSI_M2
    21:   41,     # GPIO1_B1  | SPI0_MISO_M2
    23:   43,     # GPIO1_B3  | UART4_TX_M2  | SPI0_CLK_M2
    27:   150,    # GPIO4_C6  | PWM7_IR_M3  | I2C0_SDA_M1  | SPI3_CLK_M0
    29:   63,     # GPIO1_D7  | PWM15_IR_M3  | UART1_CTSN_M1
    31:   47,     # GPIO1_B7  | PWM13_M2  | UART1_RX_M1  | SPDIF_TX_M0
    33:   103,    # GPIO3_A7  | PWM8_M0
    35:   110,    # GPIO3_B6  | CAN1_TX_M0  | PWM13_M0  | UART3_RX_M1  | I2S2_LRCK_M1
    8:    13,     # GPIO0_B5  | UART2_TX_M0  | I2C1_SCL_M0  | I2S1_MCLK_M1
    10:   14,     # GPIO0_B6  | UART2_RX_M0  | I2C1_SDA_M0  | I2S1_SCLK_M1
    12:   109,    # GPIO3_C1  | UART7_RX_M1  | SPI1_CLK_M1
    16:   100,    # GPIO3_A4
    18:   148,    # GPIO4_C4  | PWM5_M2  | SPI3_MISO_M0
    24:   44,     # GPIO1_B4  | UART7_RX_M2  | SPI0_CS0_M2
    26:   45,     # GPIO1_B5  | UART7_TX_M2  | SPI0_CS1_M2
    28:   149,    # GPIO4_C5  | PWM6_M2  | I2C0_SCL_M1  | SPI3_MOSI_M0
    32:   114,    # GPIO3_C2  | PWM14_M0  | UART7_RTSN_M1  | I2C8_SCL_M4  | SPI1_CS0_M1
    36:   105,    # GPIO3_B1  | UART2_TX_M2  | PWM2_M1
    38:   106,    # GPIO3_B2  | UART2_RX_M2  | PWM3_IR_M1  | I2S2_SDI_M1
    40:   107,    # GPIO3_B3  | UART2_RTSN  | I2S2_SDO_M1
}

# No reason for BCM mapping, keeping it for compatibility
BCM = BOARD
