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

#!/usr/bin/env python

import i2c.lcd as lcd

# use `i2cdetect` to determine device address and bus (see readme)
address = 0x27
bus = 11
lcd = lcd.display(address, bus)

# display a fake status on the four lines
lcd.display_string("geth/1.11.6-stable-e", 1)
lcd.display_string("it works!  peers: 48", 2)
lcd.display_string("   block: 17_264_799", 3)
lcd.display_string("b854e8e65..836af1984", 4)
