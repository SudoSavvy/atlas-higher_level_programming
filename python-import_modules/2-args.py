#!/usr/bin/python3
import sys

if __name__ == "__main__":
    argv = sys.argv[1:]  # Exclude the script name
    argc = len(argv)  # Get the number of arguments

    if argc == 0:
        print("Number of argument(s): 0.")
    elif argc == 1:
        print("Number of argument(s): 1 argument:")
        print("1: {}".format(argv[0]))
    else:
        print("Number of argument(s): {} arguments:".format(argc))
        for i in range(argc):
            print("{}: {}".format(i + 1, argv[i]))
