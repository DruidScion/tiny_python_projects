#!/usr/bin/env python3
"""
Picnic
"""

import argparse


def get_args():
    """
    Parse Command-line Arguments
    """
    parser = argparse.ArgumentParser(description="Picnic game")
    parser.add_argument("food", type=str, nargs="+", help="Item(s) to bring")
    parser.add_argument(
        "-s", "--sorted", default=False, metavar="SORT", help="Sort the items"
    )
    return parser.parse_args()


def main():
    """
    Main Function
    """
    args = get_args()
    food = []
    if len(args.food) == 2:
        food = args.food[0] + " and " + args.food[1]
    else:
        food = args.food[0]
    print(f"You are bringing {food}.")


if __name__ == "__main__":
    main()
