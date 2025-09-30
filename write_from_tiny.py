# -*- coding: utf-8 -*-
"""
Write from Tiny (`write_from_tiny.py`)
write scores in musicXML from the
tiny notation and associated metadata in the central json doc.

Author: Mark Gotham
Licence: MIT
"""

__author__ = "Mark Gotham"


import json
from music21 import clef, converter, expressions, key, metadata, meter, note, stream
from pathlib import Path
from typing import Optional


orig_part_list = ["superius", "contra", "tenor", "bassus"]
mod_part_list = ["S", "A", "T", "B"]
mod_to_orig_map = [2, 0, 1, 3]  # ["S": "tenor", "A": "superius", "T":"contra", "B": "bassus"]


modern_to_orig = {
    "S": "tenor",
    "A": "superius",
    "T": "contra",
    "B": "bassus"
}

orig_to_modern = {}
for i in modern_to_orig:
    orig_to_modern[modern_to_orig[i]] = i  # reverse dict


def corpus_from_json_tiny(
        write_orig: bool = True,
        write_modern: bool = True,
) -> None:
    with open("./goudimel.json", "r") as data:
        data = json.load(data)
        for item in data:
            print(item["psalm_number"])
            psalm_number = str(item["psalm_number"]).zfill(3)
            if "superius" in item:  # ready to go
                if write_orig:
                    write_orig_from_tiny(item)
                if write_modern:
                    write_modern_from_tiny(item)
            else:
                print("No copy of psalm number", psalm_number)


def write_orig_from_tiny(data: dict):
    """Write one orig version of a score from the json tinyNotation."""
    s = stream.Score()
    for i in range(4):
        name = orig_part_list[i]
        p = converter.parse("tinyNotation: 2/2 " +  data[name])
        p.partName = name

        # Clef
        c = p.recurse().getElementsByClass(clef.Clef).first()
        c.sign = data["clefs"][i][0]
        c.line = int(data["clefs"][i][1])
        p.insert(0, c)

        # Key signature
        if data["orig_key"]:
            p.insert(0, key.KeySignature(-1))  # always one flat or nothing

        # Time signature display symbol
        p.recurse().getElementsByClass(meter.TimeSignature).first().symbol = "cut"  # here, not supported in tiny

        # Last note. Special case due to tiny notation encoding.
        last_note = p.recurse().notesAndRests[-1]
        # last_note.duration.quarterLength = 8  # Either this double length (if so, also move the double barline).
        last_note.expressions.append(expressions.Fermata())  # Or this.

        p.makeMeasures(inPlace=True)
        p.makeTies(inPlace=True)

        s.insert(p)

    metadata_and_finish(s, data, original=True)


def write_modern_from_tiny(data: dict):
    """Write one orig version of a score from the json tinyNotation."""
    s = stream.Score()
    for i in range(4):
        modern_name = mod_part_list[i]
        orig_name = modern_to_orig[modern_name]

        p = stream.Part()
        p.name = modern_name
        p.insert(key.KeySignature(data["mod_sharps"]))
        p.insert(meter.TimeSignature("4/4"))
        t = data["mod_trans"]
        if modern_name == "S":
            t += 12
        elif modern_name == "T":
            p.insert(clef.Treble8vbClef())  # the others work it out by themselves ;)
        for n in converter.parse("tinyNotation: 2/2 " + data[orig_name]).recurse().notesAndRests:
            if n.isRest:
                new_note = note.Rest()
            else:
                new_note = note.Note()
                new_note.pitch = n.pitch.transpose(t)
            new_note.quarterLength = n.quarterLength / 2
            p.append(new_note)
        p.notesAndRests.last().quarterLength *= 2  # TODO CHECK
        p.makeMeasures(inPlace=True)
        p.makeTies(inPlace=True)
        s.insert(0, p)

    metadata_and_finish(s, data, original=False)


def metadata_and_finish(
        s: stream.Score,
        data: dict,
        original: bool = True,
        format: str = ".mxl",
        out_base_path: Optional[Path] = None
) -> None:
    psalm_number = str(data["psalm_number"])
    s.insert(0, metadata.Metadata())
    s.metadata.title = f'Psalm {psalm_number}: {data["title"]}'
    s.metadata.composer = 'Claude Goudimel'

    psalm_number = psalm_number.zfill(3)

    if out_base_path is None:
        out_base_path = Path('.', 'Pseaumes')
    out_path = out_base_path / psalm_number

    if original:
        when = "original"
    else:
        when = "modern"

    s.write(format, out_path / f"Goudimel_{psalm_number}_{when}{format}")


if __name__ == '__main__':
    corpus_from_json_tiny()
