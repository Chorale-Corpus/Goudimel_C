# -*- coding: utf-8 -*-
"""
NAME
===============================
Syllables (`syllables.py`)


BY
===============================
Mark Gotham


LICENCE:
===============================
MIT


ABOUT:
===============================
Basic script for retrieving syllables from syllabified text (.txt) and related sources,
as relevant to this meta-corpus (e.g., tinyNotation).
"""


from pathlib import Path
import re


__author__ = "Mark Gotham"



def text_to_syllables_lines(
    txt_path: Path
) -> list:
    """
    Take any text file and split up each line
    by spaces and hyphens
    to reveal the number of syllables.
    Separate the values into lists of lists by verse and return that
    numerical list of lists.
    """
    all_verses = []
    this_verse = []
    with open(txt_path) as file:
        lines = file.readlines()
        for line in lines:
            split_text = re.split(r'[- ]', line)
            if len(split_text) > 2:
                this_verse.append(len(split_text))
            else:  # para break
                all_verses.append(this_verse)
                this_verse = []

    return all_verses


def text_to_syllables_Goudimel(
    psalm_number: int
) -> list:
    """
    A wrapper for Goudimel-specific cases.

    >>> text_to_syllables_lines(1)
    [[10, 10, 11, 11, 10, 10], [10, 10, 11, 10, 10, 10], [10, 10, 10, 10, 10, 10]]
    """
    num_padded = str(psalm_number).zfill(3)
    txt_path = Path(".") / "Pseaumes" / num_padded / f"Goudimel_{num_padded}.txt"
    return text_to_syllables_lines(txt_path)


if __name__ == '__main__':
    import doctest
    doctest.testmod()
