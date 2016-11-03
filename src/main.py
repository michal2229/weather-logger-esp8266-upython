import dht, machine
import utime
from upysh import *

verbose = True


# import network
# nic = network.WLAN(network.STA_IF)
# nic.active(True)
# nic.connect('ssid1', 'pass1')


#utime.sleep(1)

# input pin for measuring voltage with ADC (0V .. 3V3)
pin0  = machine.Pin(0, mode=machine.Pin.IN)

# output status LED pin 
pin14 = machine.Pin(14, mode=machine.Pin.OUT)

# ADC object configured for pin 0
adc = machine.ADC(0) # not used much so far, for testing purposes

# pressure and temperature sensor object
d = dht.DHT11(machine.Pin(4))

# filename of log file
measurement_file_name = "log"

# software timer 1
tim1 = machine.Timer(-1)

# software timer 2
tim2 = machine.Timer(-1)


# function to write current measurement to log file
def dht11_write_measurement():
    with open(measurement_file_name, 'a') as f:
        d.measure() # take measurement
        if verbose:
            print(d.temperature(), d.temperature()*"#", d.humidity())
        f.write('{}, {}, {}\n'.format(utime.time(), d.temperature(), d.humidity()))


# function to init log file and soft timer callback to log periodically
def dht11_init_measurement(tsleep, timer):
    print(" >> initializing dht11 measurement")
    with open(measurement_file_name, 'a') as f:
        f.write('time, temperature, humidity\n')
        tim.init(period=int(tsleep*1000), mode=machine.Timer.PERIODIC, callback=lambda t:dht11_write_measurement())
    
    
# sleep 2 seconds to give time to press cancel button
# it is useful if one need to do something different on module than
# let it log measurements
utime.sleep(2)
print("pin0: {}".format(pin0.value()))
print("voltage: {}".format(adc.read()/1023.0))

# if button is not pressed, then init measurements    
if pin0.value() == 0:
    dht11_init_measurement(1, tim)



