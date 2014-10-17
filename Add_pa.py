#!/usr/bin/env python
## Adding -PA to the end of each line

import os,sys

outputfile = str(sys.argv[2]) 

f = open(sys.argv[1],'rU')

for line in f:
    jersey = ''
    line = line.rstrip()
    w = open(outputfile,'a')
    jersey = line + '-PA'
    print >>w,jersey
