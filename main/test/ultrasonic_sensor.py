
import time
import RPi.GPIO as GPIO

GPIO. setmode (GPIO.BOARD)
GPIO.setwarnings(False)

trig_pin = 3      
echo_pin = 5
lft_light = 8
ryt_light = 11

GPIO. setup (echo_pin,GPIO.IN)
GPIO. setup (trig_pin,GPIO.OUT)
GPIO. setup (lft_light,GPIO.OUT,initial=GPIO.HIGH)
GPIO. setup (ryt_light,GPIO.OUT,initial=GPIO.HIGH)

#GPIO.output(buzz_pin,GPIO.LOW)

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
        if (distance < 20):
            GPIO.output(lft_light,GPIO.LOW)
            GPIO.output(ryt_light,GPIO.LOW)
            print("stop")
        else:
            GPIO.output(lft_light,GPIO.HIGH)
            GPIO.output(ryt_light,GPIO.HIGH)
            print("moving")
        time. sleep (0.5)
        return distance

if __name__ == '__main__':
    try:
        while True:
            dist = distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(0.1)
            
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
