import RPi.GPIO as GPIO
from time import sleep

# Pins for Motor Driver Inputs
MotorE = 27

Motor1A = 18
Motor1B = 23

Motor2A = 17
Motor2B = 22

def setup():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)         # GPIO Numbering

    GPIO.setup(MotorE,GPIO.OUT)    # All pins as Outputs

    GPIO.setup(Motor1A,GPIO.OUT)
    GPIO.setup(Motor1B,GPIO.OUT)

    GPIO.setup(Motor2A,GPIO.OUT)
    GPIO.setup(Motor2B,GPIO.OUT)

def loop():

    GPIO.output(MotorE,GPIO.LOW)

def destroy():
    GPIO.cleanup()

if __name__ == '__main__':     # Program start from here
    setup()
    try:
        loop()
    except KeyboardInterrupt:
        destroy()