# i2c-lcd-ethereum
# Copyright (C) q9f 2014-2023
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <http://www.gnu.org/licenses/>.


import i2c.i2c as i2c
from time import sleep

# default LCD address and port (use i2cdetect to determine device)
ADDRESS = 0x27
BUS = 2

# commands
LCD_CLEARDISPLAY = 0x01
LCD_RETURNHOME = 0x02
LCD_ENTRYMODESET = 0x04
LCD_DISPLAYCONTROL = 0x08
LCD_CURSORSHIFT = 0x10
LCD_FUNCTIONSET = 0x20
LCD_SETCGRAMADDR = 0x40
LCD_SETDDRAMADDR = 0x80

# flags for display entry mode
LCD_ENTRYRIGHT = 0x00
LCD_ENTRYLEFT = 0x02
LCD_ENTRYSHIFTINCREMENT = 0x01
LCD_ENTRYSHIFTDECREMENT = 0x00

# flags for display on/off control
LCD_DISPLAYON = 0x04
LCD_DISPLAYOFF = 0x00
LCD_CURSORON = 0x02
LCD_CURSOROFF = 0x00
LCD_BLINKON = 0x01
LCD_BLINKOFF = 0x00

# flags for display/cursor shift
LCD_DISPLAYMOVE = 0x08
LCD_CURSORMOVE = 0x00
LCD_MOVERIGHT = 0x04
LCD_MOVELEFT = 0x00

# flags for function set
LCD_8BITMODE = 0x10
LCD_4BITMODE = 0x00
LCD_2LINE = 0x08
LCD_1LINE = 0x00
LCD_5x10DOTS = 0x04
LCD_5x8DOTS = 0x00

# flags for backlight control
LCD_BACKLIGHT = 0x08
LCD_NOBACKLIGHT = 0x00

En = 0b00000100  # Enable bit
Rw = 0b00000010  # Read/Write bit
Rs = 0b00000001  # Register select bit


class display:
    """
    Class to control an I2C LCD display
    """

    def __init__(self, address=ADDRESS, bus=BUS):
        """Setup the display, turn on backlight and text display + ...?"""
        self.device = i2c.device(address, bus)

        self.write(0x03)
        self.write(0x03)
        self.write(0x03)
        self.write(0x02)

        self.write(LCD_FUNCTIONSET | LCD_2LINE | LCD_5x8DOTS | LCD_4BITMODE)
        self.write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
        self.write(LCD_CLEARDISPLAY)
        self.write(LCD_ENTRYMODESET | LCD_ENTRYLEFT)
        sleep(0.2)

    def strobe(self, data):
        """clocks EN to latch command"""
        self.device.write_cmd(data | En | LCD_BACKLIGHT)
        sleep(0.0005)
        self.device.write_cmd(((data & ~En) | LCD_BACKLIGHT))
        sleep(0.001)

    def write_four_bits(self, data):
        self.device.write_cmd(data | LCD_BACKLIGHT)
        self.strobe(data)

    def write(self, cmd, mode=0):
        """write a command to lcd"""
        self.write_four_bits(mode | (cmd & 0xF0))
        self.write_four_bits(mode | ((cmd << 4) & 0xF0))

    def display_string(self, string, line):
        """write an entire string to line number"""
        if line == 1:
            self.write(0x80)
        if line == 2:
            self.write(0xC0)
        if line == 3:
            self.write(0x94)
        if line == 4:
            self.write(0xD4)

        for char in string:
            self.write(ord(char), Rs)

    def clear(self):
        """clear lcd and set to home"""
        self.write(LCD_CLEARDISPLAY)
        self.write(LCD_RETURNHOME)

    def backlight_off(self):
        """turn off backlight, anything that calls write turns it on again"""
        self.device.write_cmd(LCD_NOBACKLIGHT)

    def backlight_on(self):
        """turn on backlight"""
        self.device.write_cmd(LCD_BACKLIGHT)

    def display_off(self):
        """turn off the text display"""
        self.write(LCD_DISPLAYCONTROL | LCD_DISPLAYOFF)

    def display_on(self):
        """turn on the text display"""
        self.write(LCD_DISPLAYCONTROL | LCD_DISPLAYON)
