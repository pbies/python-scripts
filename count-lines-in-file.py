#!/usr/bin/env python
def _count_generator(reader):
	b = reader(1024 * 1024)
	while b:
		yield b
		b = reader(1024 * 1024)

###

with open('h:\\blockchain\\debug.log', 'rb') as fp:
	c_generator = _count_generator(fp.raw.read)
	count = sum(buffer.count(b'\n') for buffer in c_generator)
	print('Total lines:', count + 1)

input("Press Enter to continue...")

###

def count_lines(file):
	return sum(1 for line in open(file, 'r'))

###

cnt=sum(1 for line in open("input.txt", 'r'))
