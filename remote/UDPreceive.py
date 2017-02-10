import socket
import RPi.GPIO as GPIO
import time
#set up GPIO using BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(14, GPIO.OUT)
GPIO.setup(15, GPIO.OUT)
GPIO.setup(18, GPIO.OUT)
GPIO.setup(17, GPIO.IN)

GPIO.output(14, 0) 
GPIO.output(15, 0) 
GPIO.output(18, 0) 
GPIO.output(18, 1) 
#GPIO.output(15, 1) 

UDP_IP = "192.168.40.210"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #internet
					socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))


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

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	if(data == "1"):
		changeLights()
		time.sleep(13)

GPIO.cleanup()



	
#while True:
#	if(GPIO.input(17)==1):
#		time.sleep(0.00015)
#		if(GPIO.input(17)==1):
#			changeLights()
#			time.sleep(13)


