#!/usr/bin/env python
## dN/dS pipeline of files with Sequence.fa and Peptide.fa tags

import os, sys, subprocess

rootdir ='/Users/Muskavitch_Lab/Desktop/Orthogroups/'

f = open(sys.argv[1],'rU')

root ="'http://cegg.unige.ch/orthodbmoz2/fasta.fasta?ogs="
address =''
baseseq = 'curl -o /Users/Muskavitch_Lab/Desktop/Orthogroups/'

peptide = '/Peptide.fa '
sequence = '/Sequence.fa '

cmd = ''


seqcds = "&seqtype=cds'"
seqpep = "&seqtype=pep'"
website = ''
change = ''

for line in f:
    line = line.strip()
    change = rootdir
    os.makedirs(line)
    
    website = root
    website += str(line)
    website += str(seqcds)
    website.replace("\n", "")
    
    print website
    
    cmd = ''
    cmd = baseseq + line + sequence + website    
    os.system(cmd)
    
    website = root
    website += str(line)
    website += str(seqpep)
    website.replace("\n", "")
    
    cmd = ''
    cmd = baseseq + line + peptide + website    
    os.system(cmd)
    
  



