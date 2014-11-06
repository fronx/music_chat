# -*- coding: utf-8 -*-
import base
import time
import tones
import sys

port = 5001
the_tones = tones.from_message(raw_input("looper: "))

while True:
  for tone in the_tones:
    if tone:
      base.send(port, "looper" + ",10," + str(tone))
    time.sleep(0.1)
