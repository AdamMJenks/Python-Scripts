#!/usr/bin/env python
## For determing the number of alignments of novel genes/lncRNAs to each species
## In conjunction with the RNA-seq projecy

import os,sys

outputfile = str(sys.argv[2])

f = [line.strip() for line in open(sys.argv[1])]

w = open(outputfile,'a')
print >>w, sys.argv[1], f
