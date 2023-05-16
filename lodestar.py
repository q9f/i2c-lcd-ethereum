#!/usr/bin/env python

from eth.consensus import Consensus
import i2c.lcd as lcd
from time import sleep

# use `i2cdetect` to determine device address and bus (see readme)
address = 0x27
bus = 11
lcd = lcd.display(address, bus)

# Connect to a local Lodestar node
lodestar = Consensus("http://localhost:9596")

# Run the script in an endless loop to update the LCD
while True:
    # Only resume if the lodestar node is connected
    if lodestar.is_connected():
        # Let's try to handle as many exceptions as possible
        try:
            # Print the client version on line 1, limit to 20 chars
            line_one = lodestar.version[0:20].lower()
            line_one = line_one.rjust(20, " ")

            # Get a syncing indicator
            sync_indicator = "b:"
            if lodestar.is_syncing():
                sync_indicator = "syn:"

            peer_count_fmt = "p:" + lodestar.peer_count()
            block_number_fmt = sync_indicator + lodestar.latest_block_number()

            # Format line 2 with peer count and block number
            num_chars = len(block_number_fmt) + len(peer_count_fmt)
            num_spaces = 20 - num_chars
            line_two = peer_count_fmt + num_spaces * " " + block_number_fmt
            line_two = line_two.rjust(20, " ")

            # Format line 3 with latest block hash
            line_three = "h:" + lodestar.latest_block_hash()
            line_three = line_three.rjust(20, " ")

            # Format line 4 with latest block time
            block_time_fmt = lodestar.latest_block_time().strftime("%Y-%m-%d %H:%M:%S")
            line_four = "t:" + block_time_fmt[1:19]
            line_four = line_four.rjust(20, " ")

        # Handle CTRL+C, clear the LCD, and break the loop
        except KeyboardInterrupt:
            lcd.clear()
            break

        # Handle i2c device errors (install i2c-tools and kernel modules)
        except FileNotFoundError:
            print("error: 210 - can't find device: check i2c kernel modules")
            sleep(10)

        # Handle handle IO errors (check the serial ports and connections)
        except OSError:
            print("error: 220 - os exception: check i2c i/o and display wiring")
            sleep(10)

        # Handle all other errors and try to write on the display
        except:
            lcd.clear()
            lcd.write_line("error: 300", 1)
            lcd.write_line("python exception", 2)
            print("error: 300 - python exception")
            sleep(10)

        # Print client status if no error occured
        else:
            lcd.write_line(line_one, 1)
            lcd.write_line(line_two, 2)
            lcd.write_line(line_three, 3)
            lcd.write_line(line_four, 4)
            print(" ".join([line_one, line_two, line_three, line_four]))
            sleep(0.5)

    # Print client status if lodestar node is disconnected
    else:
        lcd.clear()
        lcd.write_line("error: 100", 1)
        lcd.write_line("lodestar disconnectd", 2)
        print("error: 100 - lodestar disconnected: check deamon")
        sleep(10)
