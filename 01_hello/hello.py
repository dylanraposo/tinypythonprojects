#!/usr/bin/env python3
"""
Author : Dylan Raposo 
Date   : 2023-02-03
Purpose: Say Hello!
"""

import argparse as ap


# --------------------------------------------------
def get_args():
    """Get command-line arguments"""

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


#     parser = ap.ArgumentParser(description='Say hello')
#     parser.add_argument('-n', '--name', default='World', help='Name to greet')
#     return parser.parse_args()


# # --------------------------------------------------
# def main():
#     """Make a jazz noise here"""

#     args = get_args()
#     print('Hello, ' + args.name + '!')


#     parser.add_argument('positional',
#                         metavar='str',
#                         help='A positional argument')

#     parser.add_argument('-a',
#                         '--arg',
#                         help='A named string argument',
#                         metavar='str',
#                         type=str,
#                         default='')

#     parser.add_argument('-i',
#                         '--int',
#                         help='A named integer argument',
#                         metavar='int',
#                         type=int,
#                         default=0)

#     parser.add_argument('-f',
#                         '--file',
#                         help='A readable file',
#                         metavar='FILE',
#                         type=ap.FileType('rt'),
#                         default=None)

#     parser.add_argument('-o',
#                         '--on',
#                         help='A boolean flag',
#                         action='store_true')

#     return parser.parse_args()


# # --------------------------------------------------
# def main():
#     """Make a jazz noise here"""

#     args = get_args()
#     str_arg = args.arg
#     int_arg = args.int
#     file_arg = args.file
#     flag_arg = args.on
#     pos_arg = args.positional

#     print(f'str_arg = "{str_arg}"')
#     print(f'int_arg = "{int_arg}"')
#     print('file_arg = "{}"'.format(file_arg.name if file_arg else ''))
#     print(f'flag_arg = "{flag_arg}"')
#     print(f'positional = "{pos_arg}"')


# # --------------------------------------------------
# if __name__ == '__main__':
#     main()
