# Untitled - By: arist - lun. janv. 25 2021

import select
from pyb import UART

uart = UART(1, 9600, timeout_char=1000)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1, timeout_char=1000) # init with given parameters


while(1):

    data = uart.readline()
    if data == 1 :
       led.on()
       time.sleep(150)
       led.off()
       time.sleep(100)
       led.on()
       time.sleep(150)
       led.off()
       time.sleep(600)
    if data == 2 :
        led.on()
        time.sleep(1000)
        led.off()
        time.sleep(1000)
        led.on()
        time.sleep(1000)
        led.off()
        time.sleep(1000)

    else :

        led.off()
