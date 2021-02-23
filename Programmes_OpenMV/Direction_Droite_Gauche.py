import pyb, time

from pyb import Pin, Timer

s1 = pyb.Servo(3)
s2 = pyb.Servo(2)

i = 0;


while(1):

    s1.angle(30)        # move servo 1 to 45 degrees
    time.sleep(2000)


    s1.angle(0)        # move servo 1 to 45 degrees
    time.sleep(2000)

    s1.angle(-40)        # move servo 1 to 45 degrees
    time.sleep(2000)


    s1.angle(0)        # move servo 1 to 45 degrees
    time.sleep(5000)
