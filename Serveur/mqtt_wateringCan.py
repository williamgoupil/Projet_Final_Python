"""
Fichier: Serveur/mqtt_wateringCan.py

Dependencies:
    sudo pip install -r Projet_Final_Python/requirements.txt
    mosquitto
"""
import logging
import signal
import sys
import json
from time import sleep
from gpiozero import Device, PWMLED
from gpiozero.pins.pigpio import PiGPIOFactory
import paho.mqtt.client as mqtt
import RPi.GPIO as GPIO                                                              
import time
from objet import camera
from objet import humiditySensor
from objet import pump
from objet import waterLevelSensor


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
TOPIC = "watering"                                                                                   
client = None  # initialise le client mqtt     

# initialize object
newCamera = camera
newHumiditySensor = humiditySensor(18) # mettre la pin approprié
newWaterLevelSensor = waterLevelSensor(18) # mettre la pin approprié
newPump = pump(18) # mettre la pin approprié


# Fonction relié au GPIO
def init_wateringCan():
    GPIO.setmode(GPIO.BCM)


# rajouter nos fonctions 





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


def on_disconnect(client, user_data, disconnection_result_code):                               
    logger.error("Déconnecté du broker MQTT")


def on_message(client, userdata, msg):                                                         
    logger.debug("Message recu pour le topic {}: {}".format( msg.topic, msg.payload))

    data = None

    try:
        data = json.loads(msg.payload.decode("UTF-8"))                                         
    except json.JSONDecodeError as e:
        logger.error("JSON Decode Error: " + msg.payload.decode("UTF-8"))
    
    #exemple de récupération de topic et d'envoi dans la bonne fonction
    """
    if msg.topic == TOPIC:
        if data['button'] == "alarme":
            alarme()
        elif data['button'] == "light":
            light()
        elif data['button'] == "door":
            door()
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
    """
    try :
        blink()
    finally:
        destroy()
    """
    #signal.pause()
