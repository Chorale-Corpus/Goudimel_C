# Goudimel, Claude: The Geneva Psalter

The Geneva Psalter is a setting of the 150 Psalm texts for 4-part choir.
This repository provides data about all 150 Psalms
as well as a selection of full-transcriptions for 41 cases from the collection.
These 41 were selected to provide the corresponding scores 
for harmonic analyses originally by Dmitri Tymoczko and provided on
Gotham et al.'s [When in Rome meta-corpus of harmonic analysis](https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/Early_Choral/Goudimel%2C_Claude/Psalmes).
As the keys and time values differ, this source records the original source in music21's `tinyNotation`
along with the transpositions needed to match the analyses.
Both "ancient" and "modern" versions of the scores (generated from the json)
are provided here.
More details follow below.


## External, Original Source, 1564

Claude Goudimel's contribution (1564) is to add harmonies
to an existing, melody-only "Genevan Psalter" which dates back further still:
The first source dates from 1539, containing a selection of psalms.
The text in all cases is a "metrical" French version of the psalm.
Goudimel's setting is based on "metrical" French text by Clément Marot and Théodore de Bèze.

The source for this transcription of the Goudimel:
[is the earliest available on IMSLP from 1564 (click here)](https://imslp.org/wiki/150_Pseaumes_de_David,_1564_(Goudimel,_Claude))
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

Note also that IMSLP provides a
[comparison of sources using the Genevan Psalter melodies here.](https://imslp.org/wiki/List_of_collections_containing_the_Genevan_Psalter_melodies)

This original source is set out in the "Choirbook format" that was common at the time.
This allows for all four voices to read from the same double page.
This layout is neither like the modern score (all parts together) nor modern parts (all parts on separate documents).
Perhaps the closest modern equivalent is the four-hands piano format where two players (primo and secondo)
play from on the same piano and read from the same double page.


## Local encodings ... in json

In describing this repo, we begin with the main point of reference
from which all secondary sources automatically derive: [`goudimel.json`](./goudimel.json).

This contains the following keys for _all_ 150:
- `title`: `str`. Original French titles (note the old language and spelling) that sets the file's alphabetical order.
- `orig_bass`: `str`. The pitch name with octave (e.g, "C4" - not to be confused with the clefs) of the first note in the original bass part.
- `orig_key`: `bool`. The original key signature expressed as a bool: there is either no key signature or one of a single flat.
- `clefs`: `list`. The four original clefs, specifying the `sign` and `line` in order (from low to high). E.g., ["G2", "C3", "C3", "F4"].
- `psalm_number`: `int`. A number in the range 1--150.
- `latin_title`: `str`. A corresponding Latin name for the psalm.
This is potentially useful for cross-referencing
(for which see also [`titles.py`](./titles.py) module
which includes a mapping between the numbering schemes
and [`psalms_texts.tsv`](./psalms_texts.tsv) file with both numbering schemes and an English translation).

Additionally, for those with full transcription, there is the following:
- string (text) representations of the original parts in music21's tinyNotation.
  - The key is given by the part name: `superius`, `contra`, `tenor`, `bassus`.
  - The values are expressed in music21's `tinyNotation` for the music of that part. 
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
- Final notes are usually double the length.
  - Here we add a fermata.
  - Alternatives include doubling the length on rendering.
- This range of clefs is not supported in tiny notation. They are added from data in the json.
- Time signature symbol. Tiny notation supports the concept of `2/2` but the symbol is added later.

"Modern" means
- still open score (though with a script provided to adapt to short score)
- modern part names: SATB
- modern clefs: treble, treble, treble8, bass
- tenor cantus firmus moved to the top-most part (now named "S")
- halved note values
- transposed to keys match up with the harmonic analyses on [When in Rome](https://github.com/MarkGotham/When-in-Rome/tree/master/Corpus/Early_Choral/Goudimel%2C_Claude/Psalmes)


## Metadata, then and now

After the frontispiece and a prefatory note, the source provides two tables of contents.
This first is alphabetical:
```
TABLE DES PSEAVMES
SELON L'ORDRE DE
L'Alphabeth
```

The metadata on this repository
(at [`goudimel.json`](./goudimel.json))
is similarly ordered by name as described above.

The second index of the source provides
'the order in which they are sung in the Church of Geneva' (my translation):
```
TABLES POVR TROU-
VER LES PSEAVMES SELON
l'ordre qu'on les chante en l'Eglise de Ge-
neve, tant apres le selon coup de la cloche,
qu'au commencement & à la fin du sermon
le Dimanche au matin & soir,&
ausi le Mecredi jour
des prieres.

ON CHANTE LES COM-
mandemens de Dieu (Leve le cœur, ouvre
l'aureille, Exode 20.) apres le sermon, le jour 
qu'on celebre la sainte Cene de nostre Sau-
veur Iesus Christ: laquelle on celebre qua-
tre fois l'an: [á] savoir, A P[â]que[s], A la Pente-
c[ô]te, Au premier Dimanche de Septembre,
& au plus prochain Dimanche de la Nati-
vité de notre Seigneur Iesus. On
chante en l'action de graces
le cantique de Simeon,
Or laisses, Crea-
teur. Luc
2.
```


## Text(s)

Each score sets out the music for one strophe of text
(most psalms consist of many strophes, repeating the music).
This repo likewise provides one strophe of text for each transcribed score.
Two cases (psalms 1 and 3) have full text as proof of concept for testing the syllabic division across verses.

Line divisions are determined by the text (punctuation break and/or capitalisation)
and/or a rest in the music.

All spelling and punctuation is preserved from the original,
except for standard (minimal) adjustments, such as:
- "u" -> "v" (e.g., as in "couuerts" -> "couverts")
- "ō" -> "on" or "om" ("cōbien" -> "combien")
- "ct" -> "t" ("poinct" -> "point")
- Apparent errors or inconsistencies between versions ("cestui-là" -> "celui-là")
- Modernised spelling ("Loy" -> "Loi", "Roy" -> "Roi")
- Abbreviations ("&" -> "et")

For comparison, this repo also includes:
- `titles.py` with scripts for mapping between different numbering systems for Psalms, Latin titles, and more.
- `psalms_texts.tsv` file with an English language version of the psalms (KJV) and both major numbering systems in full.

Various sources are other versions of the Psalm texts.
These include WikiSource's provision of:
- [A more modern French translation (1910)](https://fr.wikisource.org/wiki/Bible_Segond_1910/Livre_des_Psaumes)
- [The Latin Vulgate](https://la.wikisource.org/wiki/Vulgata_Clementina/Liber_Psalmorum)


## Scripts

The code here serves to:
- `write_from_tiny`: render scores from tiny notation as described above.
- `write_to_tiny`: extract a tiny notation version from a score.
- `corpus_conversion`: use musescore to convert between any supported formats
- `clef_tree`: produce a summary of clefs used and their counts as described below.
- `titles`: navigating two main numbering systems, Latin titles, the `psalms_texts.tsv` file, and more.

## Clefs

This shows the:
- choice of two clefs per part for S, C, and T, and 3 for B.
- Very uneven use of these combinations. For instance, C1,C3,C4,F4 is used 88 times; while C1,C3,C4,F3 appears once.

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

## Licence

Rendered scores (musicXML etc.) are CC0.
All code and other resources on this repo are MIT.


## Other file formats

Information related to one and the same chorale is represented in multiple variants and formats.
Each comes with its own advantages and disadvantages and users should make informed choices.
Filenames function as IDs in this context in the sense that files representing (information from)
the same chorale share the same filename prefix.

### Authoritative file format: MSCX

At the moment, only one file format in this dataset can be trusted to contain the full amount of 
information to the highest degree of accuracy: the uncompressed MuseScore files ending on 
`.mscx` which can be opened with MuseScore 3 or 4.
To date, we allow modification of these files using 
[MuseScore version 3.6.2](https://github.com/musescore/MuseScore/releases/tag/v3.6.2) exclusively.
However, we use the latest version of MuseScore 4 
(v4.4.4 at the time of writing this in February 2025) to convert these files to MEI and musicXML.
Apart from these format, the information from the MuseScore files is accessible by means of 
tabular files in TSV format, 3 per chorale: `*.notes.tsv`, `*.measures.tsv`, and `*.chords.tsv`
(although the naming of the last is misleading as it contains mainly markup, lyrics, bass figures, etc.).

The latest version of the Python library `ms3` is used to batch convert the MuseScore files
to other formats (`ms3 convert`) and to extract score information to TSV files (`ms3 extract`).

### MEI

To date, MuseScore 4 is able to convert files to MEI Basic 5.0 format. Take these files with a 
grain of salt as we cannot guarantee congruence with the source files.
The quality of these files makes them unsuitable for music research but they may serve as a 
starting point for a well-curated scholarly edition.
In the long run, provided the maturing of the relevant tools, the MEI files should take on 
the role of being the authoritative format.
Until then, they should not be manually modified because they are to be re-generated by conversion
and overwritten once the authoritative MuseScore files are modified.

### musicXML

For convenience and in addition, we offer the chorales in musicXML format. However, experience
shows that musicXML files output by MuseScore come with a number of issues and conversion errors.
These files are unsuited for scholarly work but some users may still appreciate their availability.

### TSV files

Tab-separated files are a dialect of CSV files and can be used the exact same way.
The most convenient way of viewing them is through a spreadsheet program such as LibreOffice Calc
(Excel, Numbers, Sheets, etc.) or a text editor with TSV support/plugin.
Power users may want to load them in their favourite programming language or statistical software.

You can look up what any column means in the documentation of ms3: https://ms3.readthedocs.io/columns

The most important TSV file is called `metadata.tsv`. It contains one row per chorale,
and comes with a number of columns that describe the piece in numerous ways.
A synoptic overview of the most important columns can be found 
[here](https://dcmlab.github.io/mozart_piano_sonatas/#how-to-read-metadata-tsv).

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
