#!/usr/bin/env python3
def key_value(mydict, find_code, find_key, return_value):
	for key in mydict:
		if key[find_code] == find_key:
			return key[return_value]
	return None
