#!/usr/bin/python3
i = ord('a')
while i <= ord('z'):
	if (i == 'q') | (i == 'e'):
		continue
	print(chr(i), end="")
	i += 1
