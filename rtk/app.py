try:
    import RPi.GPIO as GPIO     # type: ignore
except ImportError:
    import RTk.GPIO as GPIO     # type: ignore
#from RTk import GPIO
from time import sleep#, time

LED = 22

GPIO.setmode(GPIO.BCM)
GPIO.setup(LED,GPIO.OUT)

while True:
    GPIO.output(LED,1)
    sleep(1)
    GPIO.output(LED,0)
    sleep(1)
