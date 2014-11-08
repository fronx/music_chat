#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
funktionen, mit denen du dein eigenes chat-basiertes programm
schreiben kannst
"""
import sys
import socket
from subprocess import Popen

def send(port, message):
  """
  sendet eine nachricht an alle computer im lokalen netzwerk.

  port:    die nummer des programms, das auf der anderen seite lauscht
  message: ein beliebiger text
  """
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  for ip in _network_addresses():
    try:
      sock.sendto(message, (ip, port))
    except socket.error as e:
      pass

def receive(port, react_fn):
  """
  lauscht auf nachrichten

  port:     die nummer, unter der nachrichten erwartet werden

  react_fn: eine beliebige funktion, die auf nachrichten reagiert.

            react_fn muss genau einen parameter ("data") haben.
            wenn react_fn aufgerufen wird, enthält "data" die
            nachricht, die gesendet wurde.

  sobald ein programm auf nachrichten lauscht, kann es nichts
  anderes mehr tun.
  """
  sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  ip = "0.0.0.0"
  print("empfänger lauscht auf %s" % _ip_address())
  sock.bind((ip, port))
  while True:
    data, addr = sock.recvfrom(100)
    try:
      react_fn(data)
    except BaseException as e:
      print "# data: " + data
      print "# error:", str(e)

def play(length, frequency):
  """
  spielt einen ton mit einer bestimmten länge und frequenz (tonhöhe).

  length:    länge des tons in sekunden
  frequency: tonhöhe in Hz

  funktioniert nur unter mac os!
  die sox library muss installiert sein.
  """
  cmd = 'play --null --channels 1 synth %s sine %s 2&>/dev/null' % (length, frequency)
  print(cmd)
  _run(cmd)

# DETACHED_PROCESS = 0x00000008
def _run(cmd):
  Popen(cmd,shell=True,stdin=None,stdout=None,stderr=None,close_fds=True)
  # ,creationflags=DETACHED_PROCESS

def _ip_address():
  return socket.gethostbyname(socket.gethostname())

def _network_address_parts():
  return _ip_address().split('.')[0:3]

def _network_addresses():
  return [ '.'.join(_network_address_parts() + [str(i)]) for i in range(1,254) ]
