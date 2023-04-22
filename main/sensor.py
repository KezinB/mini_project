
import time
import RPi.GPIO as GPIO

GPIO. setmode (GPIO.BOARD)
GPIO.setwarnings(False)

trig_pin = 3      
echo_pin = 5

GPIO. setup (echo_pin,GPIO.IN)
GPIO. setup (trig_pin,GPIO.OUT)

def distance():
    while True:
        GPIO. output (trig_pin, True)
        time. sleep (0.00001) 
        GPIO. output (trig_pin, False)
        while GPIO. input (echo_pin) == 0:
            pass
        start = time. time ()
        while GPIO. input (echo_pin) == 1:
            pass
        end = time. time ()
        distance = ((end - start) * 34300) / 2
        time. sleep (0.5)
        return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()