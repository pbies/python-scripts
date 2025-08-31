#!/usr/bin/env python3

import sys
import base64
from tqdm import tqdm
from tqdm.contrib.concurrent import process_map

with open("list.txt","rb") as f:
	content = f.read().splitlines()

with open("suf.txt","rb") as g:
	suf = g.read().splitlines()

o = open('list-suf.txt','wb')

def go(line1):
	for line2 in suf:
		o.write(line1+line2+b'\n')

process_map(go, content, max_workers=24, chunksize=10000)

print('\a',end='',file=sys.stderr)
