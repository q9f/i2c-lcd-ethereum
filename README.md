# i2c-lcd-ethereum
iic bus scripts for monitoring ethereum nodes using serial 20x4 lcd displays

[![screenshot of two lcd displays](.github/screenshot.png)](.github/screenshot.png)

### setup

* requires `python3`
* requires `smbus2` and `web3`

```bash
pip3 install smbus2 web3
```

i2c and lcd drivers are provided in `./lib`

### credits

license: `gplv3`

drivers adapted from:
* https://github.com/sweetpi/python-i2c-lcd
* https://github.com/hardkernel/i2c_20x4_lcd
