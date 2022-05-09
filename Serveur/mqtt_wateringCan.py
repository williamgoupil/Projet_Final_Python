"""
Fichier: Serveur/mqtt_wateringCan.py

Dependencies:
    sudo pip install -r Projet_Final_Python/requirements.txt
    mosquitto
"""
import sys
sys.path.insert(0, '/objet/')

import logging
import signal
import sys
import json
import base64
from time import sleep
from gpiozero import Device, PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO                                                         
import time
import objet.camera as camera
from objet.camera import *


# initialise l'enregistrement
logging.basicConfig(level=logging.WARNING)  # configuration d'enregistrement globale 
logger = logging.getLogger("main")  # utilisateur pour ce module
logger.setLevel(logging.INFO) # Debugging pour ce fichier


# initialise GPIO
Device.pin_factory = PiGPIOFactory() # Set GpioZero pour Pi par defaut

# Variables Globales
BROKER_HOST = "localhost"  #Mettre l'adresse IP ici du serveur                                                                    
BROKER_PORT = 1883
CLIENT_ID = "WateringCanClient"                                                                         
TOPIC = "projet/watering/+"                                                                                   
client = None  # initialise le client mqtt     

# initialize object
#newCamera = camera()
#newHumiditySensor = humiditySensor(18) # mettre la pin approprié
#newWaterLevelSensor = waterLevelSensor(18) # mettre la pin approprié
#newPump = pump(18) # mettre la pin approprié


# Fonction relié au GPIO
def init_wateringCan():
    GPIO.setmode(GPIO.BCM)


# rajouter nos fonctions 
def loopSendData():
    global client
    #newHumiditySensor, newWaterLevelSensor, client
    while True:
        #humidityValue = newHumiditySensor.getHumidity()
        #waterLevelValue = newWaterLevelSensor.getWaterLevel()

        humidityValue = 10
        waterLevelValue = 10

        humidityString = (str(humidityValue) + '%')
        waterLevelString= (str(waterLevelValue) + '%')
        
        publish(client, 'projet/watering/HL', {"humidity" : humidityString})
        time.sleep(1)
        publish(client, 'projet/watering/WL' , {"waterLevel" : waterLevelString})
        time.sleep(5)

# Capture camera
def captureCamera():
    global newCamera

    newCamera.removeImg('../mosquitto_www/img', 'image.jpeg')
    newCamera.capture()

    """
    data = {}
    with open('../mosquitto_www/img/image.jpeg', mode='rb') as file:
        img = file.read()
    data['img'] = base64.encodebytes(img).decode('utf-8')

    publish(client, 'projet/watering/img', data)
    """

# Fonctions et callback relié a MQTT
def on_connect(client, user_data, flags, connection_result_code):                              
    if connection_result_code == 0:                                                            
        # 0 = connection réussie
        logger.info("Connecté au broker MQTT")
    else:
        # connection raté
        logger.error("Non connectée au broker MQTT: " + mqtt.connack_string(connection_result_code))

    # Subscribe pour un topic
    client.subscribe(TOPIC, qos=2)    


# deconnecter
def on_disconnect(client, user_data, disconnection_result_code):                               
    logger.error("Déconnecté du broker MQTT")


# A changer
def publish(client, topic, message):
    result = client.publish(topic, json.dumps(message))
    status = result[0]
    if status == 0:
        print(f"message sent to '{topic}'")
    else:
        print(f"Failed to send message to '{topic}'")


def on_message(client, userdata, msg):                                                         
    logger.debug("Message recu pour le topic {}: {}".format( msg.topic, msg.payload))

    #data = None

    """
    try:
        data = json.loads(msg.payload.decode("UTF-8"))                                         
    except json.JSONDecodeError as e:
        logger.error("JSON Decode Error: " + msg.payload.decode("UTF-8"))
    """    
    
    #exemple de récupération de topic et d'envoi dans la bonne fonction
    if msg.topic == "projet/watering/img":
        #captureCamera()
        print('Camera capture')
    
    if msg.topic == "projet/watering/pump":
        #newPump.startPump()
        print('Starting pump')

    """
    else:
        logger.error("Unhandled message topic {} with payload " + str(msg.topic, msg.payload))
    """


def destroy():
    GPIO.cleanup()

def signal_handler(sig, frame):
    logger.info("Control + C. deconnection...")
    client.disconnect() # Deconnection
    destroy()
    sys.exit(0)



def init_mqtt():
    global client
    # Connecté.
    client = mqtt.Client(                                                                      
        client_id=CLIENT_ID,
        clean_session=False)

    client.enable_logger()                                                                     

    client.on_connect = on_connect                                                             
    client.on_disconnect = on_disconnect
    client.on_message = on_message

    client.connect(BROKER_HOST, BROKER_PORT)                                                   

# Initialise Module
init_mqtt()

if __name__ == "__main__":
    signal.signal(signal.SIGINT, signal_handler)  # Capture Control + C                        
    logger.info("Ecoute pour les messages sur le topic :  '" + TOPIC + "'. Control + C pour quitter.")
    
    client.loop_start()    

    #thread ?
    try :
        loopSendData()
    finally:
        destroy()
    #signal.pause()
