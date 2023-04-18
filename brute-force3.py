#!/usr/bin/env python3

from itertools import chain, product

def bruteforce(charset, maxlength):
	return (''.join(candidate)
		for candidate in chain.from_iterable(product(charset, repeat=i)
		for i in range(1, maxlength + 1)))
