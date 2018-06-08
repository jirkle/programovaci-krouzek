#!/usr/bin/env python3

import sys

if len(sys.argv) < 2:
	print("usage:\n\t%s file [files...]" % (sys.argv[0]))

for filename in sys.argv[1:]:
	with open(filename) as f:
		print("Reading file %s" % (filename))
		data = f.read()
		print(data,end='')
		print("-----EOF-----")
