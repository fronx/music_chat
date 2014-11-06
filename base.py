import sys
import socket
from subprocess import Popen

DETACHED_PROCESS = 0x00000008

def run(cmd):
  Popen(cmd,shell=True,stdin=None,stdout=None,stderr=None,close_fds=True)
  # ,creationflags=DETACHED_PROCESS

addresses = [ "192.168.1." + str(i) for i in range(1,254) ]
sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

def send(port, message):
  for ip in addresses:
    try:
      sock.sendto(message, (ip, port))
    except socket.error as e:
      pass

def receive(port, react_fn):
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  ip = "0.0.0.0"
  sock.bind((ip, port))
  while True:
    data, addr = sock.recvfrom(100)
    try:
      react_fn(data)
    except BaseException as e:
      print "# data: " + data
      print "# error:", str(e)

def play(length, frequency):
  cmd = 'play --null --channels 1 synth %s sine %s 2&>/dev/null' % (length, frequency)
  print(cmd)
  run(cmd)
