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
    parser.add_argument("word", help="A word to describe the sighting")
    return parser.parse_args()


def main():
    """
    Main Function
    """
    args = get_args()
    article = ""
    if args.word[0].lower() in "aeiou":
        article = "an"
    else:
        article = "a"
    print(f"Ahoy, Captain, {article} {args.word} off the larboard bow!")


if __name__ == "__main__":
    main()
