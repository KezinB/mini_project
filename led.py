import RPi.GPIO as GPIO
import time

# Set the GPIO mode
GPIO.setmode(GPIO.BOARD)

# Define the LED pin
LED_PIN1 = 8
LED_PIN2 = 7# Replace with the GPIO pin number you have connected the LED to

# Set the LED pin as output
GPIO.setup(LED_PIN1, GPIO.OUT)
GPIO.setup(LED_PIN2, GPIO.OUT)

# Blink the LED
try:
    while True:
        # Turn on the LED
        GPIO.output(LED_PIN1, GPIO.HIGH)
        GPIO.output(LED_PIN2, GPIO.HIGH)
        time.sleep(1)
        # Turn off the LED
        GPIO.output(LED_PIN1, GPIO.LOW)
        GPIO.output(LED_PIN2, GPIO.LOW)
        time.sleep(1)# Delay for 1 second

except KeyboardInterrupt:
    # Clean up GPIO on keyboard interrupt (Ctrl+C)
    GPIO.cleanup()
_