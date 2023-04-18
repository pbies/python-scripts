#!/usr/bin/env python3

from string import letters, digits
strs = letters + digits
from itertools import product

def pwd_checker(pwd):
	if 0 <len(pwd) <5:
		for i in xrange(1,5):
			for per in product(strs, repeat = i):
				if "".join(per) == pwd:
					print 'your password is', "".join(per)
					return
	else:
		print "Password's length must be between 1 to 4"
