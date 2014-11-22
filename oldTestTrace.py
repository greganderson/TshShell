#!/usr/bin/python

import sys
import os

args = sys.argv

if len(args) == 1:
	print './testTrace <trace number>'
	exit(1)

if len(args) == 2:
	os.system('clear')
	print 'Test' + args[1]
	print
	print '/***************** My code *****************/'
	os.system('make test' + args[1])
	print
	print '/***************** Correct *****************/'
	os.system('make rtest' + args[1])
	print
	print 'Done.'


if len(args) == 3:
	start = int(args[1])
	end = int(args[2])
	for i in range(end - start + 1):
		os.system('clear')
		test = str(start + i)
		if len(test) == 1:
			test = '0' + str(test)
		print 'Test' + test
		print
		print '/***************** My code *****************/'
		os.system('make test' + test)
		print
		print '/***************** Correct *****************/'
		os.system('make rtest' + test)
		print
		print 'Done.'
		raw_input()
