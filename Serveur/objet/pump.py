import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BCM)

class Pump:
    def __init__(self, pump_pin):
        self.pump_pin = pump_pin
        GPIO.setup(self.pump_pin, GPIO.OUT)


    def start(self):
        GPIO.output(self.pump_pin, GPIO.HIGH)

    def stop(self):
        GPIO.setup(self.pump_pin, GPIO.OUT)


    def test(self):
        self.start()

        time.sleep(1)

        self.stop()

        GPIO.cleanup()