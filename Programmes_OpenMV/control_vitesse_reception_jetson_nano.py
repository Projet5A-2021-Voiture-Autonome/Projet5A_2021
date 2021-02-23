import select
from pyb import UART, Pin, Timer

uart = UART(3, 9600, timeout_char=1000)                         # init with given baudrate
uart.init(115200, bits=8, parity=None, stop=1, timeout_char=1000) # init with given parameters

def speed_control(vitesse):
    p = pyb.Pin("P9")
    m1_tm = Timer(1)
    m1_pwm = m1_tm.channel(1, m1_tm.PWM, pin=p, pulse_width_percent=vitesse)

while True:
    data = uart.readline()
    if data is not None:
        print("\n")

        if data == b'1' :
            print("panneau 20km/h \n")
            print("speed at 4.10")
            speed_control(4.10)

        elif data == b'2' :
            print("panneau 60km/h \n")
            print("speed at 6.75")
            speed_control(6.75)
        elif data == b'3' :
            print("panneau STOP \n")
            print("speed at 0")
            speed_control(0)
        elif data == b'4' :
            print("panneau 70km/h \n")
            print("speed at 7")
            speed_control(7)
        elif data == b'5' :
            print("panneau 80km/h \n")
            print("speed at 7.5")
            speed_control(7.5)
        elif data == b'6' :
            print("panneau 120km/h \n")
            print("speed at 8.5")
            speed_control(8.5)

        else  :
            print("non reconnu \n")






