import sys
import os
import RPi.GPIO as GPIO
import time
import math
from ADCDevice import *

class HumiditySensor:
    def __init__(self, humidity):
        self.humidityValue = humidity
    
    def setHumidity(self, humidity):
        self.humidityValue = humidity
            
            
    def getHumidity(self, humidity):
        return self.humidityValue

    def convertValue(self, humidity):
        #code convertion
    
    
    def print(self):
        print(self.humidityValue)


