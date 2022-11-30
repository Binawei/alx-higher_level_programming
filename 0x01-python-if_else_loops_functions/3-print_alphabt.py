#!/usr/bin/python3

i = ord('a')
while i <= ord('z'):
	if (i == ord('q')) | (i == ord('e')):
		i += 1
	print("{:c}".format(i), end="")
	i += 1
