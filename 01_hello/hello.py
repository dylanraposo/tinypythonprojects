#!/usr/bin/env python3


"""
Author:  Dylan Raposo
Date:    2 / 3 / 2023
Purpose: Say hello

"""

import argparse as ap


# --------------------------------------------------
def get_args():
    """Get the command-line arguments"""

    parser = ap.ArgumentParser(description='Say hello')
    parser.add_argument('-n', '--name', default='World', help='Name to greet')
    return parser.parse_args()


# --------------------------------------------------
def main():
    """Make a jazz noise here"""

    args = get_args()
    print('Hello, ' + args.name + '!')


# --------------------------------------------------
if __name__ == '__main__':
    main()
