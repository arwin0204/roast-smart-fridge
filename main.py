#!/usr/bin/env python3
"""Roast the Smart Fridge: one line, written deterministically to /output/entry.txt."""

import os

LINE = "My smart fridge sends me a weekly report on how often I open it at midnight, like a snitch with a light inside and no friends of its own."


def write_entry(path="/output/entry.txt"):
    """Write the roast line to the entry file, deterministically.

    The file always contains exactly one line: LINE followed by a
    trailing newline, encoded as UTF-8 with Unix line endings.
    """
    os.makedirs(os.path.dirname(path), exist_ok=True)
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(LINE + "\n")


def main():
    # Keep the entry write in one place so the output is identical
    # on every run, no matter who invokes the program.
    write_entry()


if __name__ == "__main__":
    main()
