import RPi.GPIO as GPIO
import dht11
import time

# initialize GPIO
GPIO.setwarnings(False)
GPIO.setmode(GPIO.BCM)
GPIO.cleanup()

# read data using pin 25
instance = dht11.DHT11(pin = 25)
result = instance.read()

def loop():
    while(True):
        if result.is_valid():
            print("Temperature: %d C" % result.temperature)
            print("Humidity: %d %%" % result.humidity)
        else:
            print("Error: %d" % result.error_code)
        time.sleep(1)

loop()
