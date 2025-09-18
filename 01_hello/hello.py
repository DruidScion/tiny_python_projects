#!/usr/bin/env python3
"""
Purpose: Say Hello
"""

import argparse


def get_args():
    """
    Get Command-line arguments
    """
    parser = argparse.ArgumentParser(description="Say Hello")
    parser.add_argument(
        "-g", "--greet", metavar="greet", default="Hello", help="Greeting to give"
    )
    parser.add_argument(
        "-n", "--name", metavar="name", default="World", help="Name to greet"
    )
    return parser.parse_args()


def main():
    """
    Main Function
    """
    args = get_args()
    print(args.greet + ", " + args.name + "!")


if __name__ == "__main__":
    main()
