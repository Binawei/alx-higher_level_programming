#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0

    for elem in range(x):
        try:
            print("{}".format(my_list[elem]), end="")
        except:
            break
        else:
            count += 1
    print()
    return count
