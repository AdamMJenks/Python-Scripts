#!/usr/bin/env python
## dN/dS pipeline of files with Sequence.fa and Peptide.fa tags

import os
import subprocess

rootdir ='/Users/Muskavitch_Lab/Desktop/Orthogroups/'

name = ''
change = rootdir

dirList = os.listdir(rootdir)
for dir in dirList:
    if dir != ".DS_Store":
        os.chdir(rootdir)
        change = rootdir
        name = dir
        change += str(name)
        print  change
        os.chdir(change)
        os.system("clustalo -i Peptide.fa -o Protein.aln")
        print "Done Executing Protein Alignment for", name
        os.system("perl /Users/Muskavitch_Lab/Desktop/pal2nal.v14/pal2nal.pl Protein.aln Sequence.fa -output fasta > CDS_align.fa")
        print "Done Make CDS-Alignment for", name
        os.system("trimal -gt 0.4 -in CDS_align.fa -out Trimmed_align.fa")
        print "Done Trimming Alignment for", name
        os.system("raxmlHPC-SSE3 -s Trimmed_align.fa -n YES -f a -m GTRGAMMA -x 12345 -p23546 -N 100")
        print "Done Making ML Tree for", name
        os.system("/Users/Muskavitch_Lab/Desktop/paml4.7a/codeml /Users/Muskavitch_Lab/Desktop/codeml.ctl")
        print "Done calculating dN/dS for", name

print "PIPELINE COMPLETE"
