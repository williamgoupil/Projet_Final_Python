import RPi.GPIO as GPIO
import time

#from microbit import *

GPIO.setmode(GPIO.BCM)

class WaterLevelSensor:
    def __init__(self, waterLeveSensor_pin):
        self.waterLeveSensor_pin = waterLeveSensor_pin
        GPIO.setup(self.waterLeveSensor_pin, GPIO.IN)

    def getWaterLevel(self, inputSelect, adc):
        return adc.analogRead(inputSelect)
        
    def test(self):
        value = self.getWaterLevel()
        print(value)
        time.sleep(1)

    def returnWaterLevel(self):

        value = self.getWaterLevel()

        #selon la value qu'on recoie retourne un % du niveau de l'eau

        if value < 100:
            return '10%'
        elif value > 100 and value < 200:
            return '20%'
        else :
            return '100%'

        #Faire le if else lorsqu'on connais les value que retourne le waterLevel
    
    def destroy(self):
        GPIO.cleanup()