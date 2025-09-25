#!/bin/bash
for f in Pseaumes/001/*.mxl; do
  echo "Converting $f → ${f%.mxl}.krn"
  python3 -m converter21 -f musicxml -t humdrum "$f" "${f%.mxl}.krn"
done
