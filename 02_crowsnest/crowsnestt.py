#!/usr/bin/env python3

"""
Name: Dylan Raposo

Date: 

Purpose: 

"""


import argparse as ap


def get_args():
    """Get command line arguments"""

    parser = ap.ArgumentParser(
        description='Rock the Casbah',
        formatter_class=ap.ArgumentDefaultsHelpFormatter)

    parser.add_argument('word',
        metavar='object',
        help='An object argument')

    return parser.parse_args()


def main():
    """Make a jazz noise here"""

    args = get_args()

    article = "an" if args.word[0].lower() in 'aeiou' else 'a'
    print("ahoy, Captain," + article + "  " +
          args.word + " off the larboard bow!")


if __name__ == '__main__':
    main()
