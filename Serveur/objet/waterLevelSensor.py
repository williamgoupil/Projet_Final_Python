import RPi.GPIO as GPIO
import time

#from microbit import *

GPIO.setmode(GPIO.BCM)

class WaterLevelSensor:
    def __init__(self, waterLevel):
        self.waterLevel = waterLevel


    def getWaterLevel(self, inputSelect, adc):
        return self.waterLevel
        
    def setWaterLevel(self, waterLevel):
        self.waterLevel = waterLevel
            
            
    def convertValue(self, waterLevel):
        # code convertion

    def print(self):
        print(self.waterLevel)
