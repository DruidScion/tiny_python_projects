#!/usr/bin/env python3
"""
Crowsnest
"""

import argparse


def get_args():
    """
    Get Command-line Arguments
    """
    parser = argparse.ArgumentParser(description="XXXX")
    parser.add_argument("-x", metavar="xxxx", help="xxxx")
    return parser.parse_args()


def main():
    """
    Main Function
    """
    args = get_args()
    print(args.xxxx)


if __name__ == "__main__":
    main()
