"""
Basic script for retrieving syllables from syllabified text.
"""


import os
import re


__author__ = "Mark Gotham"


def text_to_syllables_lines(psalm_number: int = 1) -> list:
    """
    Take any text file and split up each line
    by spaces and hypens
    to reveal the number of syllables.
    Separate the values into lists of lists by verse.

    >>> text_to_syllables_lines(1)
    [[10, 10, 11, 11, 10, 10], [10, 10, 11, 10, 10, 10], [10, 10, 10, 10, 10, 10]]

    """
    num_padded = str(psalm_number).zfill(3)
    txt_path = os.path.join(".", "Pseaumes", num_padded, f"Goudimel_{num_padded}.txt")

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


if __name__ == '__main__':
    import doctest
    doctest.testmod()
