#!/usr/bin/env python3
"""
Picnic
"""

import argparse


def get_args():
    """
    Parse Command-line Arguments
    """
    parser = argparse.ArgumentParser(description="Picnic")
    parser.add_argument("food", help="What food to bring")
    parser.add_argument("-s", "--sorted", help="Sort list")
    return parser.parse_args()


def main():
    """
    Main Function
    """
    args = get_args()
    print(f"You are bringing {args.food}.")


if __name__ == "__main__":
    main()
