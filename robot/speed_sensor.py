import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BCM)
GPIO.setup(2,GPIO.IN)
while True:
	print GPIO.input(2)
