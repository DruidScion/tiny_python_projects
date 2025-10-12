#!/usr/bin/env python3
"""
Howler
"""

import argparse
import os


# ---------------------------------------------------------------
def get_args():
    """Parse command-line arguments"""
    parser = argparse.ArgumentParser(description="Howler")
    parser.add_argument("text", metavar="str", nargs="*", help="Input text")
    return parser.parse_args()


# ---------------------------------------------------------------
def in_file():
    """Process if the argument is a file"""
    args = get_args()
    file_text = " ".join(args.text)
    if os.path.isfile(file_text):
        with open(file_text, "rt", encoding="utf-8") as file:
            for text in file:
                file_text = "".join(text).upper()
        return file_text
    return None


# ---------------------------------------------------------------
def main():
    """Main function"""
    file_text = in_file()
    args = get_args()
    yell = " ".join(args.text).upper()
    if file_text is None:
        print(yell)
    print(file_text)


if __name__ == "__main__":
    main()
