#!/usr/bin/env python
## For determing the number of alignments of novel genes/lncRNAs to each species
## In conjunction with the RNA-seq projecy

import os,sys

AgamS1 = 0
AgamP3 = 0
AgamM1 = 0
AaraD1 = 0
AquaS1 = 0
AmelC1 = 0
AmerM1 = 0
AchrA1 = 0
AepiE1 = 0
AminM1 = 0
AculA1 = 0
AfunF1 = 0
AsteS1 = 0
AsteI2 = 0
AmacM1 = 0
AfarF1 = 0
AdirW1 = 0
AsinS1 = 0
AatrE1 = 0
AdarC2 = 0
AalbS1 = 0
Total = 0

outputfile = str(sys.argv[2]) 

f = open(sys.argv[1],'rU')

for line in f:
    line = line.rstrip()
    if(line[0] == '>'):
        if line[1:] == "AgamS1":
            AgamS1 += 1
        if line[1:] == "AgamP3":
            AgamP3 += 1
        if line[1:] == "AgamM1":
            AgamM1 += 1
        if line[1:] == "AaraD1":
            AaraD1 += 1
        if line[1:] == "AquaS1":
            AquaS1 += 1
        if line[1:] == "AmelC1":
            AmelC1 += 1
        if line[1:] == "AmerM1":
            AmerM1 += 1
        if line[1:] == "AchrA1":
            AchrA1 += 1
        if line[1:] == "AepiE1":
            AepiE1 += 1
        if line[1:] == "AminM1":
            AminM1 += 1
        if line[1:] == "AculA1":
            AculA1 += 1
        if line[1:] == "AfunF1":
            AfunF1 += 1
        if line[1:] == "AsteS1":
            AsteS1 += 1
        if line[1:] == "AsteI2":
            AsteI2 += 1
        if line[1:] == "AmacM1":
            AmacM1 += 1
        if line[1:] == "AfarF1":
            AfarF1 += 1
        if line[1:] == "AdirW1":
            AdirW1 += 1
        if line[1:] == "AsinS1":
            AsinS1 += 1
        if line[1:] == "AatrE1":
            AatrE1 += 1
        if line[1:] == "AdarC2":
            AdarC2 += 1
        if line[1:] == "AalbS1":
            AalbS1 += 1
Total = AgamS1 + AgamP3 + AgamM1 + AaraD1 + AquaS1 + AmelC1 + AmerM1 + AchrA1 + AepiE1 + AminM1 + AculA1 + AfunF1 + AsteS1 + AsteI2 + AmacM1 + AfarF1 + AdirW1 + AsinS1 + AatrE1 + AdarC2 + AalbS1
        
   
    
    
w = open(outputfile,'a')
print >>w, sys.argv[1],'\t', AgamP3,'\t', AgamS1,'\t', AgamM1,'\t',AaraD1,'\t',AquaS1,'\t', AmelC1, '\t',AmerM1,'\t', AchrA1, '\t',AepiE1,'\t',AsteI2,'\t', AsteS1, '\t',AmacM1, '\t', AculA1, '\t',AminM1, '\t',AfunF1,'\t', AdirW1, '\t', AfarF1, '\t',AatrE1, '\t',AsinS1, '\t',AalbS1, '\t',AdarC2, "\t", Total
