#!/usr/bin/env python3

from itertools import chain, product
import string

def bruteforce(charset, maxlength):
	return (''.join(candidate)
		for candidate in chain.from_iterable(product(charset, repeat=i)
		for i in range(1, maxlength + 1)))

#immediate:
print(list(bruteforce('abcde', 2)))

#iterate:
for attempt in bruteforce(string.ascii_lowercase, 4):
	print(attempt)
	# match it against your password, or whatever
	#if matched:
	#	break

***

import itertools

def brute_force(password):
	for length in range(1, len(password) + 1):
		for guess in itertools.product(range(33, 127), repeat=length):
			guess = ''.join(chr(c) for c in guess)
			if guess == password:
				return guess
	return None
