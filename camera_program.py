import RPi.GPIO as GPIO
import time
from time import sleep
from picamera2 import Picamera2, Preview
import MailProgram
import tkinter as tk
def camera():
    GPIO.setmode(GPIO.BOARD)

    TRIG = 8
    ECHO= 10

    GPIO.setup(TRIG, GPIO.OUT)
    GPIO.output(TRIG, 0)

    GPIO.setup(ECHO, GPIO.IN)

    time.sleep(0.1)
    print ("starting Measurement...")
    picam2 = Picamera2()
    camera_config = picam2.create_still_configuration(main={"size": (1920, 1080)}, lores={"size": (640, 480)}, display="lores")
    picam2.configure(camera_config)
    picam2.start_preview(Preview.QTGL)
    picam2.start()
    distance=1000
    image_taken=False
    #window2=tk.Tk()
    #label=tk.Label(master=window2, text="NaN", width=150, height=75, bg="blue", fg="white")
    #label.pack()
    time.sleep(0.1)
    while distance>60:
        GPIO.output(TRIG, 1)
        time.sleep(0.00001)
        GPIO.output(TRIG,0)

        while GPIO.input(ECHO) ==0:
            pass
        start = time.time()

        while GPIO.input(ECHO) ==1:
            pass
        stop= time.time()
        distance=((stop-start) * 17000) 
        print (distance )
        int_distance=int(distance)
        #label["text"]=f"{int_distance}"
        time.sleep(0.1)

    GPIO.cleanup()

    sleep(2)
    picam2.capture_file("/home/pi/Documents/programs/test.jpg")
    image_taken=True
    picam2.close()
    return distance
