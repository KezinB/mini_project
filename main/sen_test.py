import sensor
import time
if __name__ == '__main__':
    try:
        while True:
            dist = sensor.distance()
            print ("Measured Distance = %.1f cm" % dist)
            time.sleep(1)
 
        # Reset by pressing CTRL + C
    except KeyboardInterrupt:
        print("Measurement stopped by User")
        
