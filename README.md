# Goudimel, Claude: The Geneva Psalter

The Geneva Psalter is a setting of the 150 Psalm texts for 4-part choir.
This repository provides data about all 150 Psalms
as well as selection of full-transcriptions for 41 from the "Genevan Psalter" collection.
These 41 were selected to provide the corresponding scores 
for harmonic analyses originally by Dmitri Tymoczko and provided on the
[When in Rome meta-corpus of harmonic analysis](https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/Early_Choral/Goudimel%2C_Claude/Psalmes).
As the keys and time values differ, this source records the original in music21's `tinyNotation`
along with the transpositions needed to match DT's analyses.
Both "ancient" and "modern" versions of the scores (generated from the json)
are provided here.
More details follow below.


## External, Original Source, 1564

The source for this transcription is the earliest available on IMSLP:
[the 2nd edition, of 1564, here](https://imslp.org/wiki/150_Pseaumes_de_David,_1564_(Goudimel,_Claude))
This leads to two files for the:
- [first half here (1-68)](https://s9.imslp.org/files/imglnks/usimg/f/f2/IMSLP498673-PMLP572700-Les_Pseaumes_mis_en_rime_1565_Goudimel_Claude_btv1b525015926_1-68.pdf)
- [second half here (69-150)](https://ks15.imslp.org/files/imglnks/usimg/1/1f/IMSLP498674-PMLP572700-Les_Pseaumes_mis_en_rime_1565_Goudimel_Claude_btv1b525015926_69-150.pdf)

This source's frontispiece describes it as:

```
LES
PSEAUMES MIS
EN RIEM FRAN-
SCOISE,
PAR CLEMENT MAROT ET
Theodore de Beze.
MIS EN MUSIQUE A QUATRE
parties par Claude Goudimel.
[...]
M.D.LXV
```

Yes, the use of upper/lower case is really like that. ;)

Note also that IMSLP provides a
[comparison of sources using the Genevan Psalter melodies here.]
(https://imslp.org/wiki/List_of_collections_containing_the_Genevan_Psalter_melodies)

This original source is set out in the "Choirbook format" that was common at the time.
This allows for all four voices to read from the same double page.
This layout is neither like the modern score (all parts together) nor modern parts (all parts on separate documents).
Perhaps the closest modern equivalent is the four-hands piano format where two players (primo and secondo)
play from on the same piano and read from the same double page.


## Local encodings ... in json

In describing this repo, we begin with the main point of reference
from which all secondary sources automatically derive: `goudimel.json`.

This contains the following keys for _all_ 150:
- `title`: `str`. Original French titles (note the old language and spelling) that sets the file's alphabetical order.
- `psalm_number`: `int`. A number in the range 1--150.
- `orig_bass`: `str`. The pitch name with octave (e.g, "C4" - not to be confused with the clefs) of the first note in the original bass part.
- `orig_key`: The original key signature expressed as a bool: there is either no key signature or one of a single flat.
- `clefs`: `list`. The four original clefs, specifying the `sign` and `line` in order (from superius to basses). E.g., ["G2", "C3", "C3", "F4"].

Additionally, for the 41 transcribed so far, there is the following:
- string (text) representations of the original parts in music21's tinyNotation.
  - The key is given by the part nam-: `superius`, `contra`, `tenor`, `bassus`.
  - The values are tiny notation for the music of that part.
  - This covers all relevant data except the following which we also provide on the json:
- `mod_trans`: `int`. The number of semitones and direction (+/-) for transposing from the original to the modern key choice.
- `mod_sharps`: `int`. The key signature for the modern version, expressed as a number of sharps.
  - Note that this cannot be deduced from the transposition as we are dealing with modal sources.

## Local encodings ... in mxl

From the json data, the code renders scores in both "original" and "modern" versions.

"Original" here means that it follows the source in terms of:
- open score with one voice part per stave, (though the original is in the "Choirbook format" as discussed above)
- part names: "superius", "contra", "tenor", "bassus"
- clefs: including C-clefs like "soprano", "alto", "tenor".
- note values, moving mostly in whole notes.
- part distribution with the cantus firmus melody that Goudimel harmonised placed in the tenor (middle of the texture)
- transposition level

The original is almost entirely expressed in the json, with the exception of elements unsupported by tiny notation:
- Final notes are usual double the length.
  - Here we add a fermata.
  - Alternatives include doubling the length on rendering.
- This range of clefs is not supported. They are added from data in the json.
- Time signature symbol. Tiny notation supports the concept of `2/2` but the symbol is added later.

"Modern" means
- still open score (though with a script provided to adapt to short score)
- modern part names: SATB
- modern clefs: treble, treble, treble8, bass
- tenor cantus firmus moved to the top 
- halved note values
- transposed to keys match up with the harmonic analyses on [When in Rome](https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/Early_Choral/Goudimel%2C_Claude/Psalmes)


## Scripts

The code here serves to:
- `write_from_tiny`: render scores from tiny notation as described above.
- `write_to_tiny`: extract a tiny notation version from a score.
- `corpus_conversion`: use musescore to convert between any supported formats
- `clef_tree`: produce a summary of clefs used and their counts as described below.


## Clefs

This shows the:
- choice of two clefs per part for S, C, and T, and 3 for B.
- Very uneven use of these combinations, for instance with C1,C3,C4,F4 used 88 time as compared with C1,C3,C4,F3 just once.

```
├── superius:C1
│   ├── contra:C2 = C1,C2
│   │   ├── tenor:C3 = C1,C2,C3
│   │   │   └── bassus:F3 = C1,C2,C3,F3 = 1
│   │   └── tenor:C4 = C1,C2,C4
│   │       └── bassus:F3 = C1,C2,C4,F3 = 1
│   └── contra:C3 = C1,C3
│       └── tenor:C4 = C1,C3,C4
│           ├── bassus:C4 = C1,C3,C4,C4 = 1
│           ├── bassus:F3 = C1,C3,C4,F3 = 1
│           └── bassus:F4 = C1,C3,C4,F4 = 88
└── superius:G2
    ├── contra:C2 = G2,C2
    │   ├── tenor:C3 = G2,C2,C3
    │   │   ├── bassus:C4 = G2,C2,C3,C4 = 14
    │   │   ├── bassus:F3 = G2,C2,C3,F3 = 41
    │   │   └── bassus:F4 = G2,C2,C3,F4 = 1
    │   └── tenor:C4 = G2,C2,C4
    │       └── bassus:F3 = G2,C2,C4,F3 = 1
    └── contra:C3 = G2,C3
        ├── tenor:C3 = G2,C3,C3
        │   └── bassus:F3 = G2,C3,C3,F3 = 2
        └── tenor:C4 = G2,C3,C4
            └── bassus:F4 = G2,C3,C4,F4 = 1
```


## Overview
|     file_name     |measures|labels|
|-------------------|-------:|-----:|
|Goudimel_001_modern|      28|     0|
|Goudimel_003_modern|      33|     0|
|Goudimel_021_modern|      19|     0|
|Goudimel_025_modern|      27|     0|
|Goudimel_029_modern|      27|     0|
|Goudimel_032_modern|      35|     0|
|Goudimel_035_modern|      28|     0|
|Goudimel_036_modern|      36|     0|
|Goudimel_042_modern|      27|     0|
|Goudimel_043_modern|      20|     0|
|Goudimel_047_modern|      24|     0|
|Goudimel_049_modern|      34|     0|
|Goudimel_052_modern|      18|     0|
|Goudimel_054_modern|      28|     0|
|Goudimel_056_modern|      31|     0|
|Goudimel_060_modern|      29|     0|
|Goudimel_066_modern|      55|     0|
|Goudimel_068_modern|      36|     0|
|Goudimel_073_modern|      29|     0|
|Goudimel_075_modern|      18|     0|
|Goudimel_079_modern|      35|     0|
|Goudimel_081_modern|      14|     0|
|Goudimel_084_modern|      29|     0|
|Goudimel_089_modern|      31|     0|
|Goudimel_097_modern|      24|     0|
|Goudimel_098_modern|      28|     0|
|Goudimel_099_modern|      17|     0|
|Goudimel_101_modern|      15|     0|
|Goudimel_105_modern|      22|     0|
|Goudimel_108_modern|      29|     0|
|Goudimel_118_modern|      28|     0|
|Goudimel_119_modern|      26|     0|
|Goudimel_122_modern|      35|     0|
|Goudimel_123_modern|      27|     0|
|Goudimel_124_modern|      22|     0|
|Goudimel_127_modern|      20|     0|
|Goudimel_133_modern|      25|     0|
|Goudimel_135_modern|      19|     0|
|Goudimel_138_modern|      32|     0|
|Goudimel_140_modern|      15|     0|
|Goudimel_150_modern|      24|     0|


*Overview table automatically updated using [ms3](https://ms3.readthedocs.io/).*
