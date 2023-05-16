#!/usr/bin/env python

from eth.consensus import Consensus
from eth.execution import Execution
import i2c.lcd as lcd

# use `i2cdetect` to determine device address and bus (see readme)
address = 0x27
bus = 11
lcd = lcd.display(address, bus)

# display a fake status on the four lines
lcd.write_line("geth/1.11.6-stable-e", 1)
lcd.write_line("it works!  peers: 48", 2)
lcd.write_line("  block: #17_264_799", 3)
lcd.write_line("b854e8e65..836af1984", 4)

# List of available beacon utilities
lodestar = Consensus("http://localhost:9596")
print(lodestar.version)
print(lodestar.is_connected())
print(lodestar.is_syncing())
print(lodestar.peer_count())
print(lodestar.latest_block_hash())
print(lodestar.latest_block_number())
print(lodestar.latest_block_time())
print(lodestar.current_epoch_number())
print(lodestar.current_slot_number())
print(lodestar.current_slot_time())

# List of available evm utilities
geth = Execution("http://localhost:8545")
print(geth.version)
print(geth.is_connected())
print(geth.is_syncing())
print(geth.peer_count())
print(geth.latest_block_hash())
print(geth.latest_block_number())
print(geth.latest_block_time())
