#!/usr/bin/env python3
import sys
import os
from os import path
if not path.exists("out"):
	os.mkdir('out');
filein=open('./Inbox','r',errors='ignore');
fileout=open('/dev/null','r');
i = 0
while True:
	l=filein.readline();
	if not l:
		break;
	ss = l[0:7];
	if ss == "From - ":
		fileout.close();
		i = i + 1;
		t="%05d" % (i,);
		fileout=open('out/'+t+'.eml','a');
		print('.',end='');
		sys.stdout.flush();
	fileout.write(l);
filein.close();
fileout.close();