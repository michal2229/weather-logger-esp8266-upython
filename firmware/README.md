# MicroPython firmware

## info from [http://micropython.org](http://micropython.org)

MicroPython is a lean and efficient implementation of the Python 3 programming language that includes a small subset of the Python standard library and is optimised to run on microcontrollers and in constrained environments.

The MicroPython pyboard is a compact electronic circuit board that runs MicroPython on the bare metal, giving you a low-level Python operating system that can be used to control all kinds of electronic projects.

MicroPython is packed full of advanced features such as an interactive prompt, arbitrary precision integers, closures, list comprehension, generators, exception handling and more. Yet it is compact enough to fit and run within just 256k of code space and 16k of RAM.

MicroPython aims to be as compatible with normal Python as possible to allow you to transfer code with ease from the desktop to a microcontroller or embedded system. 

[GitHub project page](https://github.com/micropython/micropython)

## uploading to ESP8266

First, You need [**esptool**](https://github.com/themadinventor/esptool). It is a software written in Python. 

To install it using PIP, execute it in the terminal:

```bash
pip install esptool
```

Next, You need to erase flash on the device:

```bash
esptool.py --port /dev/ttyUSB0 erase_flash
```

Finally, You need to upload firmware to the module:

```bash
esptool.py --port /dev/ttyUSB0 --baud 460800 write_flash --flash_size=8m 0 firmware_filename.bin
```

You may need to tweak port, baudrate (e.g. 115200 or lower) or flash size (512k upwards) according to Your module.