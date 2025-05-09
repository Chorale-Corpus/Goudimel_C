"""
Psalm text, names, numbering:
- Latin names
- Two numbering systems ("Greek" and "Hebrew").
    - Gouidmel's numbering follows what is called "Hebrew" here.
"""

from __future__ import annotations

__author__ = "Mark Gotham"

goudimel_latin_titles_dict = {
    1: "Beatus vir qui non abiit.",
    2: "Quare fremuerunt.",
    3: "Domine, quam multiplicati?",
    4: "Cum invocarem.",
    5: "Verba mea auribus percipe.",
    6: "Domine, ne in furore.",
    7: "Domine, Deus meus.",
    8: "Domine, Dominus noster.",
    (9, 10): "Confitebor tibi, Domine.",
    11: "In Domino confido.",
    12: "Salvum me fac.",
    13: "Usquequo, Domine.",
    14: "Dixit insipiens.",
    15: "Domine, quis habitabit.",
    16: "Conserva me.",
    17: "Exaudi, Domine, justitiam.",
    18: "Diligam te, Domine.",
    19: "Coeli enarrant.",
    20: "Exaudiat te Dominus.",
    21: "Domine, in virtute tua.",
    22: "Deus Deus meus.",
    23: "Dominus regit me.",
    24: "Domini est terra.",
    25: "Ad te Domine, levavi.",
    26: "Judica me, Domine.",
    27: "Dominus illuminatio.",
    28: "Ad te, Domine, clamabo.",
    29: "Afferte Domino filii Dei.",
    30: "Exaltabo te, Domine.",
    31: "In te, Domine, speravi.",
    32: "Beati, quorum remissae sunt.",
    33: "Exultate, justi.",
    34: "Benedicam Dominum.",
    35: "Judica Domine nocentes.",
    36: "Dixit injustus ut delinquat.",
    37: "Noli aemulari.",
    38: "Domine, ne in furore.",
    39: "Dixi custodiam.",
    40: "Expectans expectavi.",
    41: "Beatus qui intelligit.",
    42: "Quemadmodum desiderat.",
    43: "Judica me Deus.",
    44: "Deus auribus nostris.",
    45: "Eructavit cor meum.",
    46: "Deus noster refugium.",
    47: "Omnes gentes plaudite.",
    48: "Magnus Dominus.",
    49: "Audite haec omnes gentes.",
    50: "Deus deorum.",
    51: "Miserere.",
    52: "Quid gloriaris in malitia.",
    53: "Dixit insipiens.",
    54: "Deus in nomine tuo.",
    55: "Exaudi, Deus.",
    56: "Miserere mei Deus, quoniam.",
    57: "Miserere mei, Deus.",
    58: "Si vere utique.",
    59: "Eripe me.",
    60: "Deus repulisti nos.",
    61: "Exaudi, Deus.",
    62: "Nonne Deo.",
    63: "Deus Deus meus, ad te.",
    64: "Exaudi Deus orationem.",
    65: "Te decet.",
    66: "Jubilate Deo omnis.",
    67: "Deus misereatur.",
    68: "Exurgat Deus.",
    69: "Salvum me fac, Deus.",
    70: "Deus in adjutorium.",
    71: "In te, Domine.",
    72: "Deus, judicium tuum.",
    73: "Quam bonus Israel Deus.",
    74: "Ut quid, Deus.",
    75: "Confitebimur tibi Deus.",
    76: "Notus in Judaea.",
    77: "Voce mea.",
    78: "Attendite.",
    79: "Deus, venerunt gentes.",
    80: "Qui regis Israel.",
    81: "Exultate Deo.",
    82: "Deus stetit.",
    83: "Deus, quis similis.",
    84: "Quam dilecta tabernacula.",
    85: "Benedixisti, Domine.",
    86: "Inclina, Domine.",
    87: "Fundamenta ejus.",
    88: "Domine, Deus salutis.",
    89: "Misericordias Domini.",
    90: "Domine, refugium.",
    91: "Qui habitat.",
    92: "Bonum est confiteri.",
    93: "Dominus regnavit.",
    94: "Deus ultionum.",
    95: "Venite exultemus.",
    96: "Cantate Domino.",
    97: "Dominus regnavit, exsulset terra",
    98: "Cantate Domino.",
    99: "Dominus regnavit, irascantur.",
    100: "Jubilate Deo.",
    101: "Misericordiam et judicium.",
    102: "Domine, exaudi.",
    103: "Benedic, anima.",
    104: "Benedic, anima.",
    105: "Confitemini Domino.",
    106: "Confitemini Domino.",
    107: "Confitemini Domino.",
    108: "Paratum cor meum.",
    109: "Deus, laudem meam.",
    110: "Dixit Dominus.",
    111: "Confitebor tibi, Domine.",
    112: "Beatus vir.",
    113: "Laudate, pueri.",
    (114, 115): "In exitu Israel.",
    116: "Dilexi.",
    116: "Credidi.",
    117: "Laudate Dominum.",
    118: "Confitemini Domino.",
    119: "Beati immaculati.",
    120: "Ad Dominum.",
    121: "Levavi oculos.",
    122: "Laetatus sum in his.",
    123: "Ad te levavi.",
    124: "Nisi quia Domini.",
    125: "Qui confidunt.",
    126: "In convertendo.",
    127: "Nisi Dominus.",
    128: "Beati omnes.",
    129: "Saepe expugnaverunt.",
    130: "De profundis.",
    131: "Domine, none est.",
    132: "Memento, Domine.",
    133: "Ecce quam bonum.",
    134: "Ecce nunc benedicite.",
    135: "Laudate nomen Domini.",
    136: "Confitemini Domino.",
    137: "Super flumina.",
    138: "Confitebor tibi Domine.",
    139: "Domine, probasti.",
    140: "Eripe me, Domine.",
    141: "Domine, clamavi.",
    142: "Voce mea.",
    143: "Domine, exaudi.",
    144: "Benedictus Dominus.",
    145: "Exaltabo te, Deus.",
    146: "Lauda, anima.",
    147: "Laudate Dominum.",
    147: "Lauda, Jerusalem.",
    148: "Laudate Dominum de caelis.",
    149: "Cantate Domino.",
    150: "Laudate Dominum in sanctis."
}


def add_titles_to_goudimel() -> None:
    import os
    import json

    metadata_path = os.path.join(".", "goudimel.json")
    with open(metadata_path, "r") as json_file:
        data = json.load(json_file)
        for item in data:
            num = item["psalm_number"]
            if num is None:
                continue
            try:
                title = goudimel_latin_titles_dict[num]
            except:
                title = goudimel_latin_titles_dict[
                    greek_to_hebrew(num)
                ]
            item["latin_title"] = title

    with open(metadata_path, "w") as json_file:
        json.dump(data, json_file, indent=4)  #, sort_keys=True)


def checks(num: int):
    if not isinstance(num, int):
        raise ValueError("The number must be an integer.")
    if num < 1:
        raise ValueError("The number must be an integer greater than 0")
    if num > 150:
        raise ValueError("The number must be an integer less than or equal to 150")


def greek_to_hebrew(num: int) -> int | tuple[int, int]:
    """
    Map from Christian numbering of the Psalms as seen in the
    Greek Septuagint and Latin Vulgate
    to the Hebrew numbering systems.

    >>> greek_to_hebrew(14)
    15

    >>> greek_to_hebrew(9)
    (9, 10)
    """
    checks(num)

    if num in range(1, 8 + 1):
        return num
    elif num == 9:  # 1 -> 2
        return 9, 10
    elif num in range(10, 112 + 1):
        return num + 1
    elif num == 113:  # 1 -> 2
        return 114, 115
    elif num in (114, 115):
        return 116
    elif num in range(116, 145 + 1):
        return num + 1
    elif num in (146, 147):  # 2 -> 1
        return 147
    elif num in range(148, 150 + 1):
        return num
    else:
        raise ValueError("Unexpected number error")

def hebrew_to_greek(num: int) -> int | tuple[int, int]:
    """
    Map from Hebrew to Greek numbering systems.

    >>> hebrew_to_greek(10)
    9

    >>> hebrew_to_greek(140)
    139

    """
    checks(num)

    if num in range(1, 8 + 1):
        return num
    elif num in (9, 10):  # 2 -> 1
        return 9
    elif num in range(11, 113 + 1):
        return num - 1
    elif num in (114, 115):  # 2 -> 1
        return  113
    elif num == 116:
        return 114, 115
    elif num in range(117, 146 + 1):
        return num - 1
    elif num == 147:  # 1 -> 2
        return 146, 147
    elif num in range(148, 150 + 1):
        return num
    else:
        raise ValueError("Unexpected number error")


if __name__ == '__main__':
    import doctest
    doctest.testmod()
