#!/usr/bin/env python3

import time

start = time.time()
for _ in range(25):
	sum([i**2 for i in range(1000000)])
end = time.time()
print(end - start)
