# i2c-lcd-ethereum
# Copyright (C) q9f 2023
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

# pip3 install web3
from datetime import datetime
from time import time
from web3.beacon import Beacon

class Consensus:
    def __init__(self, uri):
        """Initialize a beacon node with an REST API exposed at URI"""
        self.uri = uri
        self.client = Beacon(uri)
        self.version = self.client.get_version()
        self.genesis = self.client.get_genesis()

    def is_connected(self):
        """Checks if client is connected and returns HTTP 200"""
        return bool(self.client.get_health() == 200)

    def is_syncing(self):
        """Checks if client is syncing the beacon chain"""
        syncing = self.client.get_syncing()
        return bool(syncing["data"]["is_syncing"])

    def peer_count(self):
        """Gets the peer count"""
        peers = self.client.get_peers()
        peer_count = int(peers["meta"]["count"])
        return self.__format_number(peer_count)

    def latest_block_hash(self):
        """Gets the latest received non-empty block hash"""
        block_header = self.client.get_block_headers()
        block_hash = str(block_header["data"][0]["header"]["message"]["body_root"])
        return self.__format_hash(block_hash)

    def latest_block_number(self):
        """Gets the latest received non-empty block number"""
        block_header = self.client.get_block_headers()
        block_number = int(block_header["data"][0]["header"]["message"]["slot"])
        return self.__format_number(block_number)

    def latest_block_time(self):
        """Gets the latest received non-empty block time"""
        block_header = self.client.get_block_headers()
        block_number = int(block_header["data"][0]["header"]["message"]["slot"])
        genesis_time = int(self.genesis["data"]["genesis_time"])
        return datetime.fromtimestamp(int(genesis_time + block_number * 12))

    def current_epoch_number(self):
        """Gets the current epoch number since genesis"""
        genesis_time = int(self.genesis["data"]["genesis_time"])
        slot_number = int((int(time()) - genesis_time) / 12)
        epoch_number = int(slot_number / 32)
        return self.__format_number(epoch_number)

    def current_slot_number(self):
        """Gets the current slot number since genesis"""
        genesis_time = int(self.genesis["data"]["genesis_time"])
        slot_number = int((int(time()) - genesis_time) / 12)
        return self.__format_number(slot_number)

    def current_slot_time(self):
        """Gets the current slot time since genesis"""
        genesis_time = int(self.genesis["data"]["genesis_time"])
        slot_number = int((int(time()) - genesis_time) / 12)
        return datetime.fromtimestamp(int(genesis_time + slot_number * 12))

    def __format_hash(self, hash):
        formatted = hash[2:11] + ".." + hash[57:66]
        return formatted

    def __format_number(self, number):
        formatted = f"{number:_}"
        return formatted
