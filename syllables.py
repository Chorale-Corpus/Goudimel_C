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
from music21 import converter, stream
from music21.analysis import segmentByRests


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


def part_to_syllables_lines(
    part: stream.Part,
    min_note_ql: float = 1.0
) -> list[int]:
    """
    Some chorale practices are highly regular in:
    - having very syllabic settings (no melisma except for the shortest note values)
    - rests between phrases.

    This basic script applies to such cases, splitting a chorale into phrases,
    and excluding short notes, returning the number of notes (and probably therefore syllables) per phrase.

    This can be compared with other methods.
    """
    syllables_this_verse = []

    segments = segmentByRests.Segmenter.getSegmentsList(part.stripTies())
    for seg in segments:
        durs = [x for x in seg if x.duration.quarterLength >= min_note_ql]
        syllables_this_verse.append(len(durs))

    return syllables_this_verse


# -----------------------------------------------------------------------------

# Goudimel-specific

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


def score_to_syllables_Goudimel(
    psalm_number: int
) -> list:
    """
    A wrapper for Goudimel-specific cases.

    >>> syl = score_to_syllables_Goudimel(3)
    >>> syl[0]
    [6, 6, 7, 6, 6, 7, 6, 6, 7, 6, 6, 7]

    >>> syl[1]
    [6, 6, 7, 6, 6, 7, 6, 6, 7, 6, 6, 7]

    >>> syl[0] == syl[1]
    True

    """
    num_padded = str(psalm_number).zfill(3)
    this_path = Path(".") / "Pseaumes" / num_padded / f"Goudimel_{num_padded}_original.mxl"
    score = converter.parse(this_path)
    return [part_to_syllables_lines(p) for p in score.parts]


if __name__ == '__main__':
    import doctest
    doctest.testmod()
