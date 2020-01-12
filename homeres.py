import RPi.GPIO as GPIO
import dht11
import time
import datetime

# initialize GPIO
GPIO.setwarnings(True)
GPIO.setmode(GPIO.BCM)

# read data using pin 14
instance = dht11.DHT11(pin=25)

while True:
	result = instance.read()
	if result.is_valid():
		GPIO.cleanup()
		print(result.temperature)
		break


