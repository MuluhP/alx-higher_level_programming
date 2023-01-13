#!/usr/bin/python3
import sys


def main(*argv):
    index = 0
    length = len(sys.argv) - 1
    if length == 1:
        print("{:d} argument:".format(length))
    elif length == 0:
        print("{:d} arguments.".format(length))
    else:
        print("{:d} arguments:".format(length))
    for args in sys.argv:
        if (index != 0):
            print("{}: {}".format(index, args))
        index += 1


if __name__ == "__main__":
    main()
