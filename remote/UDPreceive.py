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

GPIO.output(motorRF, 0) 
GPIO.output(motorRB, 0) 
GPIO.output(motorLF, 0) 
GPIO.output(motorLB, 0) 
#GPIO.output(motorRB, 1) 

UDP_IP = "192.168.40.210"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, #internet
					socket.SOCK_DGRAM) #UDP
sock.bind((UDP_IP, UDP_PORT))


def stop():
	GPIO.output(motorRF, 0) 
	GPIO.output(motorRB, 0) 
	GPIO.output(motorLF, 0) 
	GPIO.output(motorLB, 0)
	return; 

def TurnRight():
	#stop()
	#time.sleep(0.01)
	GPIO.output(motorRF, 0) 
	GPIO.output(motorRB, 1) 
	GPIO.output(motorLF, 1) 
	GPIO.output(motorLB, 0) 
	#time.sleep(10)
	return;
	
def TurnLeft():
	#stop()
	#time.sleep(0.01)
	GPIO.output(motorRF, 1) 
	GPIO.output(motorRB, 0) 
	GPIO.output(motorLF, 0) 
	GPIO.output(motorLB, 1)
	#time.sleep(10)
	return;
	
def Forward():
	#stop()
	#time.sleep(0.01)
	GPIO.output(motorRF, 1) 
	GPIO.output(motorRB, 0) 
	GPIO.output(motorLF, 1) 
	GPIO.output(motorLB, 0) 
	#time.sleep(1)
	return;
	
def Backward():
	#stop()
	#time.sleep(0.01)
	GPIO.output(motorRF, 0) 
	GPIO.output(motorRB, 1) 
	GPIO.output(motorLF, 0) 
	GPIO.output(motorLB, 1)
	#time.sleep(1)
	return;

while True:
	data, addr = sock.recvfrom(1024) # buffer size is 1024 bytes
	#print "received message:", data
	if(data == "right"):
		TurnRight()
		print("right")
		
	elif(data == "left"):
		TurnLeft()
		print("left")
	
	elif(data == "forward"):
		Forward()
	
	elif(data == "backward"):
		Backward()
	
	elif(data == "stop"):
		stop()
		print("right")
		
GPIO.cleanup()



