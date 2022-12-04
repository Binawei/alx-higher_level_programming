#!/usr/bin/python3
def print_matrix_integer(matrix=[[]]):
    for i in matrix:
        p = 1
        for j in i:
            if p == len(i):
                print("{:d}".format(j), end="")
            else:
                print("{:d}".format(j), end=" ")
                p += 1
        print()
