import i2c.lcd as lcd

# use `i2cdetect` to determine device address and bus (see readme)
address = 0x27
bus = 2
lcd = lcd.display(address, bus)

lcd.display_string("geth/1.11.6-stable-e", 1)
lcd.display_string("it works!  peers: 48", 2)
lcd.display_string("   block: 17_264_799", 3)
lcd.display_string("b854e8e65..836af1984", 4)
