#!/usr/bin/python3
import sys
if __name__ == "__main__":
    
    argv_count = len(sys.argv)
    
    if argv_count is 1:
        print("{:d} arguments.".format(0))
    elif argv_count is 2:
        print("{:d} argument:".format(1))
        print("{:d}: {:s}".format(1, sys.argv[1]))
    else:
        print("{:d} arguments:".format(argv_count - 1))
        for index in range(1, argv_count):
            print("{:d}: {:s}".format(index, sys.argv[index]))

