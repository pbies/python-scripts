#!/usr/bin/env python3
import socket
import subprocess
import sys
import os
from datetime import datetime
from tqdm import tqdm

# Clear the screen
clear = lambda: os.system('cls')
clear()

# Ask for input
remoteServer	= input("Enter a remote host to scan: ")
remoteServerIP  = socket.gethostbyname(remoteServer)

# Print a nice banner with information on which host we are about to scan
print("-" * 60)
print("Please wait, scanning remote host", remoteServerIP)
print("-" * 60)

# Check what time the scan started
t1 = datetime.now()

# Using the range function to specify ports (here it will scans all ports between 1 and 1024)

# We also put in some error handling for catching errors

txt="Open ports: "

try:
#	for port in range(1,1025):
#		print(port)
	for port in tqdm(range(1,1025), total=len(range(1,1025)), unit="ports"):
		sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		sock.settimeout(0.2)
		result = sock.connect_ex((remoteServerIP, port))
		if result == 0:
			txt=txt+" "+str(port)
		sock.close()

except KeyboardInterrupt:
	print("You pressed Ctrl+C")
	sys.exit()

except socket.gaierror:
	print('Hostname could not be resolved. Exiting')
	sys.exit()

except socket.error:
	print("Couldn't connect to server")
	sys.exit()

# Checking the time again
t2 = datetime.now()

# Calculates the difference of time, to see how long it took to run the script
total =  t2 - t1

print(txt)

# Printing the information to screen
print('Scanning Completed in: ', total)

# Wait for key press
input("Press Enter to quit...")
