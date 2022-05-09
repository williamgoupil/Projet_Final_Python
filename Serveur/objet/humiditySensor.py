import sys
import os
import RPi.GPIO as GPIO
import time
import math
from ADCDevice import *

class HumiditySensor:
    def __init__(self, humiditySensor_pin):
        self.humiditySensor_pin = humiditySensor_pin
        GPIO.setup(self.humiditySensor_pin, GPIO.IN)
        self.setup()

            
            
    def getHumidity(self, inputSelect,adc):
        return adc.analogRead(inputSelect)

    def test(self, inputSelect):
        value = self.getHumidity(inputSelect)

        print(value)

        GPIO.cleanup()


