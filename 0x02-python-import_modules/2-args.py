#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    
    argv_count = len(sys.argv)
    #index = 1
    if argv_count is 1:
        print("{:d} arguments.".format(0))
    elif argv_count is 2:
        print("{:.0f} argument:".format(1))
        print("{:.0f}: {:s}".format(1, sys.argv[1]))
    else:
        print("{:.0f} arguments:".format(argv_count - 1))
        for index in range(1, argv_count):
            print("{:.0f}: {:s}".format(index, sys.argv[index]))
            index += 1

