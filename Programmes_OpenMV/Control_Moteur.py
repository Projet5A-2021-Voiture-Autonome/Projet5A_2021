import pyb, time, machine


from pyb import Pin, Timer

def speed_control(vitesse):


    p = pyb.Pin("P9") # P9 has TIM4, CH3
    tim = pyb.Timer(4, freq=40.1)
    ch = tim.channel(3, Timer.PWM, pin=p)
    ch.pulse_width_percent(vitesse)

while(1):


    speed_control(1)  # controle de la vitesse
    pyb.delay(1000)
    speed_control(0)
    pyb.delay(1000)