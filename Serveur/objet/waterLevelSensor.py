import RPi.GPIO as GPIO
import time

#from microbit import *

GPIO.setmode(GPIO.BCM)

class WaterLevelSensor:
    def __init__(self, waterLevel):
        self.waterLevel = waterLevel


    def getWaterLevel(self, inputSelect, adc):
        return adc.analogRead(inputSelect)
        
    def setWaterLevel(self, waterLevel):
        self.waterLevel = waterLevel
            
            
    def getWaterLevel(self, waterLevel):
        if waterLevel > 0 
        
        
        
        #return adc.analogRead(inputSelect)

    def print(self):
        print(self.waterLevel)
