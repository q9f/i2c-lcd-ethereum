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

from datetime import datetime
import eth.util as util

# pip3 install web3
from web3 import Web3
from web3.middleware import geth_poa_middleware


class Execution:
    def __init__(self, uri):
        """Initialize a beacon node with an REST API exposed at URI"""
        self.uri = uri
        self.client = Web3(Web3.HTTPProvider(uri))
        self.client.middleware_onion.inject(geth_poa_middleware, layer=0)
        self.version = self.client.client_version

    def is_connected(self):
        """Checks if client is connected"""
        return bool(self.client.is_connected())

    def is_syncing(self):
        """Checks if client is syncing the evm chain"""
        syncing = self.client.eth.syncing
        return bool(not syncing == False)

    def peer_count(self):
        """Gets the peer count"""
        peer_count = int(self.client.net.peer_count)
        return util.format_number(peer_count)

    def latest_block_hash(self):
        """Gets the latest received non-empty block hash"""
        latest_block = self.client.eth.get_block("latest")
        block_hash = latest_block.hash.hex()
        return util.format_hash(block_hash)

    def latest_block_number(self):
        """Gets the latest received non-empty block number"""
        latest_block = self.client.eth.get_block("latest")
        block_number = latest_block.number
        return util.format_number(block_number)

    def latest_block_time(self):
        """Gets the latest received non-empty block time"""
        latest_block = self.client.eth.get_block("latest")
        block_time = latest_block.timestamp
        return datetime.fromtimestamp(block_time)
