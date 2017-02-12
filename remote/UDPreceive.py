import socket
import RPi.GPIO as GPIO
import time

#set used pin for motor
motorRF = 14 
motorRB = 15
motorLF = 17
motorLB = 18

#set up GPIO using BCM
GPIO.setmode(GPIO.BCM)

GPIO.setwarnings(False)

GPIO.setup(motorRF, GPIO.OUT)
GPIO.setup(motorRB, GPIO.OUT)
GPIO.setup(motorLF, GPIO.OUT)
GPIO.setup(motorLB, GPIO.OUT)
#GPIO.setup(17, GPIO.IN)

GPIO.output(motorRF, LOW) 
GPIO.output(motorRB, LOW) 
GPIO.output(motorLF, LOW) 
GPIO.output(motorLB, LOW) 
#GPIO.output(15, 1) 

UDP_IP = "192.168.40.210"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #internet
					socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))


def stop():
	GPIO.output(motorRF, LOW) 
	GPIO.output(motorRB, LOW) 
	GPIO.output(motorLF, LOW) 
	GPIO.output(motorLB, LOW)
	return; 

def TurnRight():
	stop()
	time.sleep(0.01)
	GPIO.output(motorRF, LOW) 
	GPIO.output(motorRB, HIGH) 
	GPIO.output(motorLF, HIGH) 
	GPIO.output(motorLB, LOW) 
	time.sleep(1)
	return;
	
def TurnLeft():
	stop()
	time.sleep(0.01)
	GPIO.output(motorRF, High) 
	GPIO.output(motorRB, LOW) 
	GPIO.output(motorLF, LOW) 
	GPIO.output(motorLB, HIGH)
	time.sleep(1)
	return;
	
def Forward():
	stop()
	time.sleep(0.01)
	GPIO.output(motorRF, HIGH) 
	GPIO.output(motorRB, LOW) 
	GPIO.output(motorLF, HIGH) 
	GPIO.output(motorLB, LOW) 
	time.sleep(1)
	return;
	
def Backward():
	stop()
	time.sleep(0.01)
	GPIO.output(motorRF, LOW) 
	GPIO.output(motorRB, HIGH) 
	GPIO.output(motorLF, LOW) 
	GPIO.output(motorLB, HIGH)
	time.sleep(1)
	return;

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	print "received message:", data
	if(data == "turn right"):
		TurnRight()
		
	if(data == "turn left"):
		TurnLeft()
	
	if(data == "forward"):
		Forward()
	
	if(data == "backward"):
		Backward()
	
	if(data == "stop"):
		stop()
		
GPIO.cleanup()


