import RPi.GPIO as GPIO
from time import sleep

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)
# Define the motor pins
motor1_pin1 = 33
motor1_pin2 = 31
motor2_pin1 = 35
motor2_pin2 = 37
led1 = 3
led2 = 5
# Configure the motor pins as outputs
GPIO.setup(motor1_pin1, GPIO.OUT)
GPIO.setup(motor1_pin2, GPIO.OUT)
GPIO.setup(motor2_pin1, GPIO.OUT)
GPIO.setup(motor2_pin2, GPIO.OUT)
GPIO.setup(led1,GPIO.OUT)
GPIO.setup(led2,GPIO.OUT)


GPIO.output(led1,GPIO.LOW)
GPIO.output(led2,GPIO.LOW)
GPIO.output(motor1_pin1, GPIO.LOW)
GPIO.output(motor1_pin2, GPIO.LOW)
GPIO.output(motor2_pin1, GPIO.LOW)
GPIO.output(motor2_pin2, GPIO.LOW)
sleep(10)

def forward():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.LOW)
    print("Moving forward")
    
def backward():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.HIGH)
    print("Moving backward")
        
def rit():
    GPIO.output(motor1_pin1, GPIO.HIGH)
    GPIO.output(motor1_pin2, GPIO.LOW)
    GPIO.output(motor2_pin1, GPIO.LOW)
    GPIO.output(motor2_pin2, GPIO.HIGH)
    GPIO.output(led1,GPIO.LOW)
    GPIO.output(led2,GPIO.HIGH)
    print("Moving right")
    
def lft():
    GPIO.output(motor1_pin1, GPIO.LOW)
    GPIO.output(motor1_pin2, GPIO.HIGH)
    GPIO.output(motor2_pin1, GPIO.HIGH)
    GPIO.output(motor2_pin2, GPIO.LOW)
    GPIO.output(led1,GPIO.HIGH)
    GPIO.output(led2,GPIO.LOW)
    print("Moving left")
	
for i in range(100):
    forward()
    sleep(5)
    backward()
    sleep(5)
    lft()
    sleep(5)
    rit()
    sleep(5)


GPIO.cleanup()

