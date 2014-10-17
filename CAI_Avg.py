#!/usr/bin/env python
## For determing the number of alignments of novel genes/lncRNAs to each species
## In conjunction with the RNA-seq projecy

import os,sys


f = open(sys.argv[1],'a+b')
header = f.readline()
header = header.rstrip(os.linesep)

for line in f:
    line = line.rstrip('\n')
    if(line[0] == '>'):
        header = header[0:]
        header = line
        sequence = ''
        print header
    else:
        sequence += line
    


    

    
   