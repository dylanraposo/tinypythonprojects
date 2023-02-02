"""
Author: Dylan Raposo
Date: 2 / 3 / 2023
Purpose: The purpose of this program is to greet a user by saying hellp followed by their name. In this case, Dylan Raposo.
"""

import argparse as ap

def main():

#Get command line arguments

    parser = ap.ArgumentParser(
        description = 'Hello Mini Project',
        formatter_class = ap.ArgumentDefaultsHelpFormatter)
