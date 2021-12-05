#!/usr/bin/env python3
import sys

l = sorted(sys.stdin.readlines(), key=len)
for i in l:
    print(i, end='')
