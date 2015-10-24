#!/usr/bin/python
from flask import Flask,render_template, request, jsonify
import subprocess as sp
import RPi.GPIO as GPIO ## Import GPIO library
import sys

GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM) ## Use board pin numbering

pin = 17
GPIO.setup(pin, GPIO.OUT) ## Setup GPIO Pin 17 to OUT

def setState(newState):
	if newState==1:
		GPIO.output(17,GPIO.HIGH) ## Turn on GPIO pin 17
	elif newState==0:
		GPIO.output(17,GPIO.LOW) ## Turn off GPIO pin 17    

def state():
	if GPIO.input(pin) == True:
		return "1"
	else:
		return "0"


app = Flask(__name__)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/turn_on')
def turn_on():
#    cmd = ["sudo","python","toggle.py","1"]
#    p = sp.check_output(cmd)
	setState(1)
	return "Status: " + state()

@app.route('/turn_off')
def turn_off():
	setState(0)
	return "Status: " + state()


if __name__ == '__main__':
	app.run(debug=True)