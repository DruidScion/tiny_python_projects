#!/usr/bin/env python3
"""
Jump the five
"""

import argparse


def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Jump the five")
    parser.add_argument("word", help="Word")
    return parser.parse_args()


def main():
    """Main Function"""
    args = get_args()
    print(args.word)


if __name__ == "__main__":
    main()
