#!/usr/bin/env python3

import sys

o = open('output.txt', 'w')

for i in range(1000001):
	o.write(str(i) + "\n")
