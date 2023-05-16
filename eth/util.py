# i2c-lcd-ethereum
#
# Copyright (C) 2023 Afri Schoedon @q9f
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


def format_hash(hash):
    formatted = hash[2:10] + ".." + hash[58:66]
    return str(formatted)


def format_number(number):
    formatted = f"{number:_}"
    return str(formatted)
