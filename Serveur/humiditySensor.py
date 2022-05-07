import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class HumiditySensor:
    def __init__(self, humiditySensor_pin):
        self.humiditySensor_pin = humiditySensor_pin
        GPIO.setup(self.humiditySensor_pin, GPIO.IN)

    def getHumidity(self):
        return GPIO.input(self.humiditySensor_pin)

    def test(self):
        value = self.getHumidity()

        print(value)

        time.sleep(1)

        GPIO.cleanup()