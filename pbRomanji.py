#!/usr/bin/env python3

from romkan import *
from xerox import *
import unicodedata

DEBUG = False

CHK = unicodedata.name(paste()[0])

if DEBUG:
    print(unicodedata.name(paste()[0]))

if "KATAKANA" in CHK or "CJK" in CHK or "HIRAGANA" in CHK:
    print(to_roma(paste()))
else:
    print("First character in paste board has to be either Katakana or Hiragana or Kanji")
