#!/usr/bin/env python3

import hashlib

def sha256(b):
    return hashlib.sha256(b).digest()

def sha256hex(b):
    return hashlib.sha256(b).digest().hex()

print(sha256(b''))
print(sha256hex(b''))
