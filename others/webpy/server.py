#!/usr/bin/python
import web
import RPi.GPIO as GPIO
import time

urls = (
	'/','index'
)

class index:
	#set up GPIO using BCM
	GPIO.setmode(GPIO.BCM)

	#GPIO.setwarnings(False)

	GPIO.setup(14, GPIO.OUT)
	GPIO.setup(15, GPIO.OUT)
	GPIO.setup(18, GPIO.OUT)
	GPIO.setup(17, GPIO.IN)

	GPIO.output(14, 0) 
	GPIO.output(15, 0) 
	GPIO.output(18, 0) 
	GPIO.output(18, 1) 
	#GPIO.output(15, 1) 

	def changeLights():
        	GPIO.output(18,0)
        	GPIO.output(15,1)
        	time.sleep(1)

	        GPIO.output(15,0)
        	GPIO.output(14,1)
        	time.sleep(1)

	        GPIO.output(18,1)       
        	GPIO.output(15,0)
        	GPIO.output(14,0)
        	time.sleep(1)

	        return;


	def GET(self):
		while True:
		        if(GPIO.input(17)==1):
				time.sleep(0.00015)
				if(GPIO.input(17)==1):
					changeLights()
					time.sleep(13)

		GPIO.cleanup()

		return "Hello, World"



if __name__ == "__main__":
	app = web.application(urls, globals())
	app.run()
