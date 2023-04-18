#!/usr/bin/env python3
# send TCP from stdin
import os
import sys
import socket
import io

TCP_IP = '91.195.251.44'
TCP_PORT = 24995
BLOCK_SIZE = 1024*16

try:
	s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
	s.connect((TCP_IP, TCP_PORT))
	reader = io.open(sys.stdin.fileno(), mode='rb', closefd=False)
	while reader.readable():
		peek = reader.peek(BLOCK_SIZE)
		if len(peek) < 1:
			break
		buffer = reader.read(BLOCK_SIZE)
		s.send(buffer)
		if len(buffer) != BLOCK_SIZE:
			break
	s.close()
except Exception:
	pass
