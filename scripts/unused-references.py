#!/usr/bin/python

"""
Figuring out if you use undefined citations is easy.

However, sometimes during refactor, you end up with less references because you forgot to reference the citation
This is really bad because you mention something without citing => palgiarism
Also, it reduces the value of your research.

Ideally an IDE would do this, but haven't find a good one yet.

Usage: ./executable.py *.tex *.bib
"""

import sys
import os
import re

def _findCitationsInLine(line):
    return re.findall(r"\\cite{([^}]*)}", line)

def _findDefinitionsInLine(line):
    return re.findall(r"@[^{]+{([^,]+),", line)

def getCitations(texFiles):
    ret = {}
    for fileName in texFiles:
        with open(fileName) as fd:
            for line in fd:
                citations = _findCitationsInLine(line.rstrip("\n"))
                for citation in citations:
                    if not citation in ret:
                        ret[citation] = 0
                    ret[citation] += 1

    return ret

def getDefinitions(bibFiles):
    ret = {}
    for fileName in bibFiles:
        with open(fileName) as fd:
            content = ''.join([line.rstrip("\n") for line in fd])

            definitions = _findDefinitionsInLine(content)
            for definition in definitions:
                if not definition in ret:
                    ret[definition] = 0
                ret[definition] += 1

    return ret

def main():
    texFiles = filter(lambda s: ".tex" in s, sys.argv)
    bibFiles = filter(lambda s: ".bib" in s, sys.argv)

    if len(texFiles) == 0 or len(bibFiles) == 0:
        print "Usage: %s *.tex *.bib" % (sys.argv[0])
        sys.exit(1)

    citations = getCitations(texFiles)
    definitions = getDefinitions(bibFiles)

    print "\n\n----------------------------------------------------------------"
    print "%d/%d bibliography items cited" % (len(citations), len(definitions))

    print
    print "Definition keys not used:"
    print

    for definition in definitions:
        if not definition in citations:
            print definition
    print "----------------------------------------------------------------"


if __name__ == "__main__":
    main()


