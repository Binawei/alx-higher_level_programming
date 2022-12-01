#!/usr/bin/python3
if __name__ == "__main__":
     import sys
     argv = sys.argv[1:]
     argc = len(argv)

     n, result = 1, 0
     while n <= argc:
	   result += int(sys.argv[n])
           n += 1
     print("{:d}".format(result))
