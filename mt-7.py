#!/usr/bin/env python3

from multiprocessing import Pool
from tqdm import tqdm
import sys

max_ = int(1e4)
th = 8

def go(i):
	pass

if __name__ == "__main__":
	with Pool(processes=th) as p, tqdm(total=max_) as pbar:
		for result in p.imap(go, range(0, max_)):
			pbar.update()
			pbar.refresh()

	print('\a', end='', file=sys.stderr)
