import os 
import cv2
import subprocess

#Camera initialize
camera = cv2.VideoCapture(0)

#Button initialize
buttonPin = 20
GPIO.setmode(GPIO.BCM)
GPIO.setup(buttonPin, GPIO.IN, pull_up_down = GPIO.PUD_UP)

imageCounter = 0
while True:
    GPIO.wait_for_edge(buttonPin, GPIO.FALLING)

    ret, frame = camera.read()
    imageName = 'Pre{}.jpg'.format(imageCounter)
    cv2.imwrite(imageName, frame)
    imageCounter += 1
    print("Picture" + imageName + "is taken")