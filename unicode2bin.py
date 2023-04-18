#!/usr/bin/env python3

import binascii

outfile = open("out.txt","wb")
infile = open("in.txt","rb")

while True:
	b=infile.read(1)
	if b == b'':
		break
	if b==b'\\':
		b=infile.read(1)
		if b==b'u':
			bs=infile.read(4)
			outfile.write(binascii.unhexlify(bs).decode('utf-8').encode())
		else:
			outfile.write(b'\\')
	else:
		outfile.write(b)


outfile.close()
infile.close()
