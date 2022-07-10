#!/usr/bin/env python3
import concurrent.futures
import socket
import threading

print_lock = threading.Lock()

addr = input("Enter address or IP to scan: ")
ip = socket.gethostbyname(addr)
print("Scanning "+ip+"...\nOpen ports: ",end='')

def scan(ip, port):
	scanner = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	scanner.settimeout(0.5)
	try:
		scanner.connect((ip, port))
		scanner.close()
		with print_lock:
			print(port,end=' ',flush=True)
	except:
		pass

with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
	for port in range(1,1025):
		executor.submit(scan, ip, port)

input("\nPress Enter to quit...")
