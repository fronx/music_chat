# -*- coding: utf-8 -*-
import base
import time

port = 5001
name = raw_input("wie heißt du? ")

def to_tone(key):
  try:
    tone = {"q":  170
           ,"a":  200
           ,"w":  250
           ,"s":  300
           ,"e":  400
           ,"d":  500
           ,"r":  600
           ,"f":  700
           ,"t":  800
           ,"g":  900
           ,"y": 1000
           ,"h": 1100
           ,"u": 1200
           ,"j": 1300
           ,"i": 1400
           ,"k": 1500
           ,"o": 1600
           ,"l": 1700
           ,"l": 1800
           }[key]
    return tone
  except:
    return None

def to_tones(message):
  return [ to_tone(key) for key in message ]

while True:
  for tone in to_tones(raw_input(name + ": ")):
    if tone:
      base.send(port, name + ",10," + str(tone))
    time.sleep(0.1)
