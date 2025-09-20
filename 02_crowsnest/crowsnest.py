#!/usr/bin/env python3
"""
Crowsnest
"""

import argparse


def get_args():
    """
    Get Command-line Arguments
    """
    parser = argparse.ArgumentParser(
        description="Crow's Nest -- choose the correct article"
    )
    parser.add_argument("word", help="A word to describe the sighting")
    return parser.parse_args()


def get_article(word: str) -> str:
    """
    Get the correct article
    """
    return "an" if word[0].lower() in "aeiou" else "a"


def main():
    """
    Main Function
    """
    args = get_args()
    article = get_article(args.word)
    print(f"Ahoy, Captain, {article} {args.word} off the larboard bow!")


if __name__ == "__main__":
    main()
