#!/usr/bin/env python3

import testname as tn

def main():

    print("in the main of testnamecall")
    print("__name__ in call program = " + __name__)
    print("now call testname")
    tn.main()

if __name__ == "__main__":
    main()




