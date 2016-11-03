# Weather logger on ESP8266 with MicroPython

Simple weather logger for ESP8266 with MicroPython firmware.

It creates a log file on device's flash memory and append weather data line by line. 
Log file can be extracted by connecting trough serial communication or using [WebREPL](https://github.com/micropython/webrepl), which may be simpler. 

It works with attached firmware version, but API is still evolving and [ESP8266 port is still experimental](https://github.com/micropython/micropython/tree/master/esp8266), so there are no guarantees it works with latest version.
