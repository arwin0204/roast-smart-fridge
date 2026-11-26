#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, written deterministically to /output/entry.txt."""

import os

LINE = "My smart fridge sends me a weekly report on how often I open it at midnight, like a snitch with a light inside and no friends of its own."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
