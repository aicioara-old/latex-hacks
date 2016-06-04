#!/usr/bin/python

"""
Script used for


Usage: ./executable.py *.tex *.bib
"""

import sys
import os

def getCitations(texFiles):
    pass

def getDefinitions(bibFiles):
    pass

def main():
    texFiles = filter(lambda s: ".tex" in s, sys.argv)
    bibFiles = filter(lambda s: ".bib" in s, sys.argv)

    if len(texFiles) == 0 or len(bibFiles) == 0:
        print "Usage: %s *.tex *.bib" % (sys.argv[0])
        sys.exit(1)

    citations = getCitations(texFiles)
    definitions = getDefinitions(bibFiles)



if __name__ == "__main__":
    main()


