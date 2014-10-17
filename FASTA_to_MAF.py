#!/usr/bin/env python
## FASTA Alignment file to Pseudo-multiple alignment file (FASTA -> MAF)

import os,sys

outputfile = str(sys.argv[2])
w = open(outputfile,'a')

print >>w, "a\t", "score=0"

f = [line.strip() for line in open(sys.argv[1])]

length = len(f)

count = 0

while count < length:
    current = f[count]
    if current[0] == ">":
        nextline = count + 1
        length = len(f[nextline])
        print >>w, "%s%s%s%s%s%s%s%s%s%s" % ('s\t',current[1:],'\t0\t', length,'\t',"+","\t",length,'\t', f[nextline])
    count += 1


