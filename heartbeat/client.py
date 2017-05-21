#!/usr/bin/python


import socket
import time

message = "hello by radision from 127.0.0.1 at device first_dev"
# host = socket.gethostname()		# get hostname, or you can set it as '0.0.0.0' or dns
host = '139.162.84.223'
port = 9977				# get port

s = socket.socket(socket.AF_INET,	# Internet
		socket.SOCK_DGRAM)	# UDP, create a socket object

while True:
  s.sendto(message, (host,port))
  time.sleep(10)
