#!/usr/bin/env python3

with open("sample.txt", "r") as a_file:
	for line in a_file:
		stripped_line = line.strip()
		print(stripped_line)
