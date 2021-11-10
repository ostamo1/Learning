#!/bin/python3
import socket
import sys
from datetime import datetime

if len(sys.argv)==2:
	target = socket.gethostbyname(sys.argv[1]) #translate port to ipv4
else :
	print ("invalid number of arguments")
	print ("syntax python3 scanner.py <ip>")
print("-" * 50)
print("scanning target "+ target)
print("Time Started: " + str(datetime.now()))
print ("-" * 50)

try:
	for port in range(50,85):
		s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port)) #returns an error indicator
		if result == 0:
			print("Port {} is open".format(port))
		s.close()
except KeyboardInterrupt:
	print("\nExiting Program")
	sys.exit()
except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
except socket.error:
	print ("Couldn't connect to server.")
	sys.exit()



