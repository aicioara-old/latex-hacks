#!/usr/bin/python

"""
Figuring out if you use undefined citations is easy.
However, sometimes during refactor, you end up with less references because you forgot to reference the citation
This is really bad because you mention something without citing => palgiarism
Also, it reduces the value of your research.

Ideally an IDE would do this, but haven't find a good one yet.

Usage: ./executable.py *.tex

Author: [Andrei Cioara](http://andrei.cioara.me)
"""

import sys
import re
import operator

from unusedReferences import *


def main():
    texFiles = filter(lambda s: ".tex" in s, sys.argv)

    if len(texFiles) == 0:
        print "Usage: %s *.tex" % (sys.argv[0])
        sys.exit(1)

    citations = getCitations(texFiles)

    maxLengthKey = 0
    maxLengthValue = 0
    for key in citations:
        maxLengthKey = max(maxLengthKey, len(key))
        maxLengthValue = max(maxLengthValue, len(str(citations[key])))

    sortedCitations = sorted(citations.items(), key=operator.itemgetter(1), reverse=True)

    for (key, value) in sortedCitations:
        print "%s - %s" % (key.ljust(maxLengthKey), str(value).ljust(maxLengthValue))


if __name__ == "__main__":
    main()


