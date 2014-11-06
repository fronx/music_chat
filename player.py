import base

def react(data):
  name, length, frequency = data.split(",")
  length = min(int(length)/10.0, 2)
  print('%s: %s,%s' % (name, length, frequency))
  base.play(length, int(frequency))

port = 5001
base.receive(port, react)
