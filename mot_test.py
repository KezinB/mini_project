import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the motor pins
IN1 = 31
IN2 = 33
IN3 = 35
IN4 = 37

# Set the motor pins as output
GPIO.setup(IN1, GPIO.OUT)
GPIO.setup(IN2, GPIO.OUT)
GPIO.setup(IN3, GPIO.OUT)
GPIO.setup(IN4, GPIO.OUT)

# Function to control motor clockwise
def motor_clockwise():
    GPIO.output(IN1, GPIO.HIGH)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.HIGH)
    GPIO.output(IN4, GPIO.LOW)

# Function to control motor counter-clockwise
def motor_counterclockwise():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.HIGH)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.HIGH)

# Function to stop motor
def motor_stop():
    GPIO.output(IN1, GPIO.LOW)
    GPIO.output(IN2, GPIO.LOW)
    GPIO.output(IN3, GPIO.LOW)
    GPIO.output(IN4, GPIO.LOW)

# Control the motor
for i in range(10000):
    motor_clockwise()  # Rotate motor clockwise
    time.sleep(2)  # Rotate for 2 seconds
    motor_stop()  # Stop motor
    time.sleep(1)  # Pause for 1 second
    motor_counterclockwise()  # Rotate motor counter-clockwise
    time.sleep(2)  # Rotate for 2 seconds
    motor_stop()  # Stop motor

# Cleanup GPIO
GPIO.cleanup()
