#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

if len(sys.argv) < 3:
	print("Mám málo parametrů")
	exit(1)

def prumer (pole):
	return (pole[-1]+pole[-2]+pole[-3])/3

stack = []

for x in sys.argv[1:]:
	num = 0
	try:
		num = float (x)
	except:
		print("Text \"{0}\" není číslo".format(x))
		continue
	stack.append(num)
	if len(stack) > 2:
		p = prumer(stack)
		print(p)
