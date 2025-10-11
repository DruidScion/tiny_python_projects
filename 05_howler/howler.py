#!/usr/bin/env python3
"""
Howler
"""

import argparse


# ---------------------------------------------------------------
def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Howler")
    parser.add_argument("text", metavar="str", nargs="*", help="Input text")
    return parser.parse_args()


# ---------------------------------------------------------------
def main():
    args = get_args()
    yell = " ".join(args.text).upper()
    print(yell)


if __name__ == "__main__":
    main()
