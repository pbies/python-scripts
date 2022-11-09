#!/usr/bin/python3

with open("1", "r") as a:
	aa=a.readlines()
	with open("2", "r") as b:
		bb=b.readlines()
		with open("3", "w") as c:
			for la in aa:
				la=la.rstrip('\n')
				for lb in bb:
					lb=lb.rstrip('\n')
					c.write(la+'.'+lb+'\n')
