#!/usr/bin/python


import socket
import time

message = "hello by radision from 127.0.0.1"
host = socket.gethostname()		# get hostname, or you can set it as '0.0.0.0' or dns
port = 9977				# get port

s = socket.socket(socket.AF_INET,	# Internet
		socket.SOCK_DGRAM)	# UDP, create a socket object

while True:
  s.sendto(message, (host,port))
  time.sleep(3)
