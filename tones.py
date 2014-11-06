def from_key(key):
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

def from_message(message):
  return [ from_key(key) for key in message ]
