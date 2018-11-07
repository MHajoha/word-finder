#!/usr/bin/env python3
import argparse
import re
from enum import Enum, auto


class SourceFormat(Enum):
    LINES = auto()
    SSV = auto()


parser = argparse.ArgumentParser()
parser.add_argument("--word-source", "-s", type=argparse.FileType("r"),
                    default="./openthesaurus.txt")
parser.add_argument("--source-format", "-f", type=SourceFormat)
parser.add_argument("string")
args = parser.parse_args()

if __name__ == '__main__':
    pattern = re.compile(r"^(\(.*\))?\s*(?P<word>" +
                         r"\w*" + r"\w*".join(args.string) + r"\w*" +
                         r")\s*(\(.*\))?$", re.IGNORECASE)

    words = []
    for line in args.word_source:
        if line.startswith("#"):
            continue

        for word in line.split(";"):
            match = pattern.match(word)
            if match:
                words.append(match.group("word"))
            else:
                continue

    for word in words:
        print(word)
