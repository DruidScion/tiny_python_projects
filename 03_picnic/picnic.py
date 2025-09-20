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
    parser.add_argument("-s", "--sorted", action="store_true", help="Sort the items")
    return parser.parse_args()


def format_output(food: list[str]) -> str:
    """
    Format the string properly for output
    """
    if len(food) == 1:
        return food[0]
    if len(food) == 2:
        return " and ".join(food)
    return ", ".join(food[:-1]) + ", and " + food[-1]


def main():
    """
    Main Function
    """
    args = get_args()
    if args.sorted:
        food = sorted(args.food)
    else:
        food = args.food
    print(f"You are bringing {format_output(food)}.")


if __name__ == "__main__":
    main()
