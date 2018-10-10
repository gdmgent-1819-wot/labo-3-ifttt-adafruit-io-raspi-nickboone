from Adafruit_IO import MQTTClient
import pygame
import time
from sense_hat import SenseHat, ACTION_PRESSED, ACTION_HELD, ACTION_RELEASED
from signal import pause
import datetime
import requests

sense = SenseHat()

ADAFRUIT_IO_USERNAME = ""
ADAFRUIT_IO_KEY = ""

def connected(client):
      client.subscribe('IFTTT_button') # or change to whatever name you used

def matrix(sense):
        sense.show_message("DRUK!", text_colour=[255, 0, 0])


def ring_creater(payload):
    pygame.mixer.init()
    pygame.mixer.music.load("Ringing-a-doorbell.mp3")
    pygame.mixer.music.play()  

def timecal(event):
    if event.action == ACTION_RELEASED:
        datetime.datetime.now()
        r = requests.get('')
        print(r.json())
    
sense.stick.direction_any = timecal

# this gets called every time a message is received
def message(client, feed_id, payload):
     if payload == "test":
        print ("Message test received from IFTTT.")
     else:
        ring_creater(payload)
        matrix(sense)

client = MQTTClient(ADAFRUIT_IO_USERNAME, ADAFRUIT_IO_KEY)

# Setup the callback functions defined above.
client.on_connect    = connected
client.on_message    = message


client.connect()
client.loop_blocking() # block forever on client loop
