
import time
import RPi.GPIO as GPIO

GPIO. setmode (GPIO.BOARD)
GPIO.setwarnings(False)

trig_pin = 3      
echo_pin = 5
lft_light = 8
ryt_light = 11
lftMot1 = 12
lftMot2 = 13
rytMot1 = 15
rytMot2 = 16

GPIO. setup (echo_pin,GPIO.IN)
GPIO. setup (trig_pin,GPIO.OUT)
GPIO. setup (lft_light,GPIO.OUT,initial=GPIO.HIGH)
GPIO. setup (ryt_light,GPIO.OUT,initial=GPIO.HIGH)
GPIO. setup (lftMot1,GPIO.OUT)
GPIO. setup (lftMot2,GPIO.OUT)
GPIO. setup (rytMot1,GPIO.OUT)
GPIO. setup (rytMot2,GPIO.OUT)

#functions
def forward():
    GPIO.output(lftMot1,GPIO.HIGH)
    GPIO.output(lftMot2,GPIO.LOW)
    GPIO.output(rytMot1,GPIO.HIGH)
    GPIO.output(rytMot2,GPIO.LOW)
    print("Moving forward....")
    
def backward():
    GPIO.output(lftMot1,GPIO.LOW)
    GPIO.output(lftMot2,GPIO.HIGH)
    GPIO.output(rytMot1,GPIO.LOW)
    GPIO.output(rytMot2,GPIO.HIGH)
    print("Moving backward....")

def rytTurn():
    GPIO.output(lftMot1,GPIO.HIGH)
    GPIO.output(lftMot2,GPIO.LOW)
    GPIO.output(rytMot1,GPIO.LOW)
    GPIO.output(rytMot2,GPIO.LOW)
    print("turn right....")
    
def lftTurn():
    GPIO.output(lftMot1,GPIO.LOW)
    GPIO.output(lftMot2,GPIO.LOW)
    GPIO.output(rytMot1,GPIO.HIGH)
    GPIO.output(rytMot2,GPIO.LOW)
    print("Moving forward....")
#motion of motors according to the sensor data
def motion(dist):
    if(dist < 20):
        backward()
    elif(dist < 30):
        rytTurn()
    elif(dist < 40):
        lftTurn()
    else:
        forward()
        
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
            motion(dist)
            time.sleep(0.1)
            
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        GPIO.cleanup()
