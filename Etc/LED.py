import RPi.GPIO as GPIO
import time
GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)
GPIO.setup(18,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(12,GPIO.OUT)
GPIO.setup(16,GPIO.OUT)
#GPIO.setup(26,GPIO.OUT)

#variable for time
i = 0.02
print "LED on"

#GPIO.output(26,GPIO.HIGH)

for x in xrange(1000):

#Bar 1 / 4  --- Beat 1 of every 4 bars = all four LEDs lighting up
	GPIO.output(18,GPIO.HIGH)
#	GPIO.output(23,GPIO.HIGH)
#	GPIO.output(12,GPIO.HIGH)
#	GPIO.output(16,GPIO.HIGH)
	time.sleep(i)
	#turn off all beat Yellow (Beat 2)
	GPIO.output(18,GPIO.LOW)
	GPIO.output(23,GPIO.HIGH)
#	GPIO.output(12,GPIO.LOW)
#	GPIO.output(16,GPIO.LOW)
	time.sleep(i)
	
	GPIO.output(23,GPIO.LOW)
	GPIO.output(12,GPIO.HIGH)
	time.sleep(i)

	GPIO.output(12,GPIO.LOW)
#	GPIO.output(16,GPIO.HIGH)
#	time.sleep(i)

#	GPIO.output(16,GPIO.LOW)	

	

#	GPIO.output(18,GPIO.HIGH)
#	time.sleep(i)

#	GPIO.output(18,GPIO.LOW)
#	GPIO.output(23,GPIO.HIGH)
#	time.sleep(i)

#	GPIO.output(23,GPIO.LOW)
#	GPIO.output(12,GPIO.HIGH)
#	time.sleep(i)

#	GPIO.output(12,GPIO.LOW)
#	GPIO.output(16,GPIO.HIGH)
#	time.sleep(i)
	
#	GPIO.output(16,GPIO.LOW)

	if x==1000:
		break;


print "LED off"

