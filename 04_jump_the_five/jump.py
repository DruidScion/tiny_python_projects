#!/usr/bin/env python3
"""
Jump the five
"""

import argparse


# ---------------------------------------------------------------
def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Jump the five")
    parser.add_argument("text", metavar="str", help="Input text")
    return parser.parse_args()


# ---------------------------------------------------------------
def encode(text: str) -> str:
    """Process text encoding"""
    table = {
        "1": "9",
        "2": "8",
        "3": "7",
        "4": "6",
        "5": "0",
        "6": "4",
        "7": "3",
        "8": "2",
        "9": "1",
        "0": "5",
    }

    output_str = []
    for char in text:
        output_str.append(table.get(char, char))
    return "".join(output_str)


# ---------------------------------------------------------------


def main():
    """Main Function"""
    args = get_args()
    print(encode(args.text))


if __name__ == "__main__":
    main()
