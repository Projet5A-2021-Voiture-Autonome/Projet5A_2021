# Black Grayscale Line Following Example
#
# Making a line following robot requires a lot of effort. This example script
# shows how to do the machine vision part of the line following robot. You
# can use the output from this script to drive a differential drive robot to
# follow a line. This script just generates a single turn value that tells
# your robot to go left or right.
#
# For this script to work properly you should point the camera at a line at a
# 45 or so degree angle. Please make sure that only the line is within the
# camera's field of view.

import sensor, image, time, math, pyb


#BINARY_VIEW = True
servo = pyb.Servo(3)    # pin P9
moteur = pyb.Servo(2)	# pin P8
x_blob1 = 0
x_blob2 = 0
y_blob1 = 0
y_blob2 = 0
compteur = 0
angle = 0
# Tracks a black line. Use [(128, 255)] for a tracking a white line.
GRAYSCALE_THRESHOLD = [(150, 255)]

# Each roi is (x, y, w, h). The line detection algorithm will try to find the
# centroid of the largest blob in each roi. The x position of the centroids
# will then be averaged with different weights where the most weight is assigned
# to the roi near the bottom of the image and less to the next roi and so on.
ROIS = [ # [ROI, weight]   ROI : Regions of interest
        (0, 100, 160, 20, 1), # You'll need to tweak the weights for your app
        (0,  20, 160, 20, 0.3) # depending on how your robot is setup.
       ]

# Compute the weight divisor (we're computing this so you don't have to make weights add to 1).
weight_sum = 0

for r in ROIS: weight_sum += r[4] # r[4] is the roi weight.

# Camera setup...

sensor.reset() # Initialize the camera sensor.
sensor.set_pixformat(sensor.GRAYSCALE) # use grayscale.
sensor.set_framesize(sensor.QQVGA) # use QQVGA for speed.
sensor.skip_frames(time = 2000) # Let new settings take affect.
sensor.set_auto_gain(False) # must be turned off for color tracking
sensor.set_auto_whitebal(False) # must be turned off for color tracking
clock = time.clock() # Tracks FPS.

while(True):
    clock.tick() # Track elapsed milliseconds between snapshots().
    img = sensor.snapshot() # Take a picture and return the image.
    #img.binary(GRAYSCALE_THRESHOLD)


    centroid_sum = 0

    for r in ROIS:
        blobs = img.find_blobs(GRAYSCALE_THRESHOLD, roi=r[0:4], merge=True) # r[0:4] is roi tuple.
        compteur = compteur + 1
        if blobs:
            # Find the blob with the most pixels.
            largest_blob = max(blobs, key=lambda b: b.pixels())

            if compteur == 1:
                x_blob1 = largest_blob.cx() #on stocke la position en x du premier blob
                y_blob1 = largest_blob.cy() #on stocke la position en y du premier blob
            if compteur == 2:
                x_blob2 = largest_blob.cx() #on stocke la position en x du deuxième blob
                y_blob2 = largest_blob.cy() #on stocke la position en y du deuxième blob
            # Draw a rect around the blob.
            img.draw_rectangle(largest_blob.rect())
            img.draw_cross(largest_blob.cx(),
                           largest_blob.cy())

            centroid_sum += largest_blob.cx() * r[4] # r[4] is the roi weight.

    compteur = 0



    deltax = x_blob2 - x_blob1 #on calcule le côté adjacent



    deltay = y_blob2 - y_blob1 #on calcule le côté opposé

    if (deltax != 0) :
        tanAngle = deltay / deltax

        angle = math.atan(tanAngle)
        angle = angle* 360/(2*3.14) #on ramène l'angle en degrée


    if angle < 0:   #on tourne a droite si l'angle < 0
        consigneAngle=  abs(abs(angle)-90) + 30 #on ramène l'angle à 0 puis defini le centre à 30 (position centrale du cerveau)
        if abs(consigneAngle) > 70 : #valeur max du servo
            consigneAngle =  70
    else :          #on tourne a gauche si l'angle > 0
        consigneAngle= -1* abs(abs(angle)-90) + 30 #on ramène l'angle à 0 puis defini le centre à 30 (position centrale du cerveau)
        if abs(consigneAngle) < -10 : #valeur min du servo
            consigneAngle = -10

    consigneDecalage = x_blob1 - 80 #le centre de l'image est 80, on ramène la coordonnée x du premier blob à zero, cette valeur traduit
                                    #le décalage de la ligne blanche en fonction du centre de l'image en y = 0

    servo.angle(consigneAngle + consigneDecalage)


