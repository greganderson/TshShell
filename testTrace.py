#!/usr/bin/python

import sys
import os
import commands


badTests = ['11', '12', '13']

def clearJobsAndPids(line):
	if '[' in line:
		line = line[0:line.index('[')+1] + line[line.index(']'):]
	if '(' in line:
		line = line[0:line.index('(')+1] + line[line.index(')'):]
	return line


def testIfCorrect(test):
	badTest = False
	if test in badTests:
		badTest = True
		print 'This script will not correctly validate this test.  Just printing output.'
		raw_input('Press enter to continue...')

	os.system('clear')
	print 'Test' + test
	print
	print '/***************** My code *****************/'
	s, o = commands.getstatusoutput('make test' + test)
	print o
	print
	print '/***************** Correct *****************/'
	s2, c = commands.getstatusoutput('make rtest' + test)
	print c

	if badTest:
		raw_input()
		return

	print
	print 'Testing for correctness...'
	print

	output = o.split('\n')
	correct = c.split('\n')

	if len(output) != len(correct):
		print 'Incorrect: Different length outputs'
		return

	for i in range(1, len(output)):
		oLine = clearJobsAndPids(output[i])
		cLine = clearJobsAndPids(correct[i])
		if oLine != cLine:
			print 'Incorrect: Strings'
			print 'Mine: ' + oLine
			print 'Correct: ' + cLine
			return
	print 'Correct!'


args = sys.argv

if len(args) == 1:
	print './testTrace <trace_number> OR ./testTrace <trace_number> <trace_number>'
	exit(0)

if len(args) == 2:
	testIfCorrect(args[1])

if len(args) == 3:
	start = int(args[1])
	end = int(args[2])
	for i in range(end - start + 1):
		test = str(start + i)
		if len(test) == 1:
			test = '0' + str(test)
		testIfCorrect(test)
		raw_input()
