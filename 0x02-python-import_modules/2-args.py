#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    argv = sys.argv[1:]
    argv_count = len(argv)
    index = 1
    if argv_count is 0:
        print("{0:.0f} arguments.".format(argv_count))
    elif argv_count is 1:
        print("{:.0f} argument:".format(argv_count))
        print("{:.0f}: {:s}".format(index, sys.argv[1]))
    else:
        print("{:.0f} arguments:".format(argv_count))
        while index <= argv_count:
            print("{:.0f}: {:s}".format(index, sys.argv[index]))
            index += 1

