import RPi.GPIO as GPIO ## Import GPIO library
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering

GPIO.setup(17, GPIO.OUT) ## Setup GPIO Pin 17 to OUT
newState = str(sys.argv[1])
if newState=="1":
    GPIO.output(17,GPIO.HIGH) ## Turn on GPIO pin 17
elif newState=="0":
    GPIO.output(17,GPIO.LOW) ## Turn off GPIO pin 17    
