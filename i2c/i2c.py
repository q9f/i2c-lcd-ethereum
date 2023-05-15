# pip3 install smbus2
import smbus2 as smbus


class device:
    def __init__(self, addr, port):
        self.addr = addr
        self.bus = smbus.SMBus(port)

    # Write a single command
    def write_cmd(self, cmd):
        self.bus.write_byte(self.addr, cmd)

    # Write a command and argument
    def write_cmd_arg(self, cmd, data):
        self.bus.write_byte_data(self.addr, cmd, data)

    # Write a block of data
    def write_block_data(self, cmd, data):
        self.bus.write_block_data(self.addr, cmd, data)

    # Read a single byte
    def read(self):
        return self.bus.read_byte(self.addr)

    # Read
    def read_data(self, cmd):
        return self.bus.read_byte_data(self.addr, cmd)

    # Read a block of data
    def read_block_data(self, cmd):
        return self.bus.read_block_data(self.addr, cmd)
