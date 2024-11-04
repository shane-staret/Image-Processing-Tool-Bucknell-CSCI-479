#!/usr/bin/env python3

import sys

def main():

    argsList = sys.argv[1:] # the first argument is the filename
    #print(argsList)

    while len(argsList) > 0:
        currentArg = argsList.pop(0) # first element in the list of flags given
        print(currentArg)


if __name__ == "__main__":
    main()
