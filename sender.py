# -*- coding: utf-8 -*-
import base
import time
import tones

port = 5001
name = raw_input("wie heißt du? ")

while True:
  for tone in tones.from_message(raw_input(name + ": ")):
    if tone:
      base.send(port, name + ",10," + str(tone))
    time.sleep(0.1)
