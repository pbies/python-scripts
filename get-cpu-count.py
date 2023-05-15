#!/usr/bin/env python3

import multiprocessing
multiprocessing.cpu_count()

###

import os
len(os.sched_getaffinity(0))
