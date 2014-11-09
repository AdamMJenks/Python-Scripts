### Smith matrix scoring for Welkin lab for evolution study of ERV
### Takes prealigned (usually CLUSTALW) amino acid fasta file as input (each sequence on single line, not multiple.  Remove wrapping)
### Use all uppercase amino acids (CLUSTAL option turn off)
### Prompt: python Smithmatrix.py [input file] [Final Output File Name] [Directory to place files] [iteration file base name]

#!/usr/bin/python

import sys
import os
import shutil


### Matrix scoring dictionary as previously published

Smithmatrixdict = {'D=D': 0,'D=E': 1,'D=K': 2,'D=R': 2,'D=H': 2,'D=N': 2,'D=Q':
2,'D=S': 2,'D=T': 2,'E=E': 0,'E=K': 2,'E=R': 2,'E=H': 2,'E=N': 2,'E=Q': 2,'E=S':
2,'E=T': 2,'K=K': 0,'K=R': 1,'K=H': 1,'K=N': 2,'K=Q': 2,'K=S': 2,'K=T': 2,'R=R':
0,'R=H': 1,'R=N': 2, 'R=S': 2,'R=Q': 2,'R=T': 2,'H=H': 0,'H=N': 2,'H=T':
2,'H=Q': 2,'H=S': 2,'N=N': 0,'N=Q': 1,'N=S': 2,'N=T': 2,'Q=Q': 0, 'Q=S':
2,'Q=T': 2,'S=S': 0, 'S=T': 1,'T=T': 0,'I=I': 0,'I=L': 1,'I=V': 1,'I=F':
2,'I=W': 2,'I=Y': 2,'I=C': 2,'I=M': 2, 'L=L': 0,'L=V': 1,'L=F': 2,'L=W':
2,'L=Y': 2,'L=C': 2,'L=M': 2,'V=V': 0,'V=F': 2,'V=W': 2,'V=Y': 2,'V=C': 2,'V=M':
2, 'F=F': 0,'F=W': 1,'F=Y': 1,'F=C': 2,'F=M': 2,'W=W': 0,'W=Y': 1,'W=C':
2,'W=M': 2,'Y=Y': 0,'Y=C': 2,'Y=M': 2,'C=C': 0, 'C=M': 2,'M=M': 0,'A=A':
0,'A=G': 1,'G=G': 0,'P=P': 0,'E=D': 1,'K=D': 2,'R=D': 2,'H=D': 2,'N=D': 2,'Q=D':
2,'S=D': 2, 'T=D': 2,'K=E': 2,'R=E': 2,'H=E': 2,'N=E': 2,'Q=E': 2, 'S=E':
2,'T=E': 2,'R=K': 1,'H=K': 1,'N=K': 2,'Q=K': 2,'S=K': 2,'T=K': 2,'H=R': 1,'N=R':
2,'S=R': 2,'Q=R': 2,"T=R": 2, 'N=H': 2,'T=H': 2,'Q=H': 2,'S=H': 2,'Q=N':
1,'S=N': 2,'T=N': 2,'S=Q': 2,'T=Q': 2,'T=S': 1,'L=I': 1,'V=I': 1,'F=I': 2,
'W=I': 2,'Y=I': 2,'C=I': 2,'M=I': 2,'V=L': 1,'F=L': 2,'W=L': 2,'Y=L': 2,'C=L':
2,'M=L': 2,'F=V': 2,"W=V": 2,'Y=V': 2, 'C=V': 2,'M=V': 2,'W=F': 1,'Y=F':
1,'C=F': 2,'M=F': 2,'Y=W': 1,'C=W': 2,'M=W': 2,'C=Y': 2,'M=Y': 2,'M=C': 2,'G=A':
1}


### Commandline arguements

inputfile = str(sys.argv[1])
outputfile = str(sys.argv[2])
directname = str(sys.argv[3])
basename = (str(sys.argv[4]))

if os.path.exists(directname):          ###Remove old directory incase redoing program
    shutil.rmtree(directname)
    
os.mkdir(directname)                    ###Make directory told in argument 3

file = open(inputfile, 'r')

linelist = [line.strip() for line in open(sys.argv[1])]  ### All lines in the fasta file (sequences and IDs), strip lines 


count = len(linelist)           ### Number of lines in fasta file for looping purposes

consensus = tuple(linelist[1])  ### Not actually consensus, just first sequence in the list used to initialize the score(k) function, what's compared to
amino = len(consensus)          ### Peptide length to use for looping purposes

### Create empty lists that will be used to compare all of the sequences 

comparelist = list()            ### Store the tuple of each comparison ie. A=A etc.
exper = list()                  ### To hold the new sequence to be compared to the consensus
total = list()                  ### Total score up to that loop iteration
initial = list()                ### First list


### Function to get the score when comparing a sequence elements between two successive sequences
### The default score if not in the list is 3 indicating the elements being compared are very different

def score(k):
    if consensus[k] == '-':
        score = 0
    elif consensus[k] != '-' and exper[k] == '-':
        score = 3
    elif consensus[k] != '-' and exper[k] != '-':
        score = Smithmatrixdict.get(pair, 3)
    return score
    
### Loop through each of the sequences that are in the input fasta file

for i in range(3,count,2):
    exper = linelist[i]                                                 ### Exper list is now the new sequence for each loop
    print linelist[i-1], 'ANALYZED'                                     ###QC so the user know what is being analyzed
    
    ### Loop through each amino acid to be compared in consensus and exper list
    
    for k in range(0,amino-1):
        
        if i == 3:                                                      ### For first loop to fill all of the lists
            comparelist.append(consensus[k] + '=' + exper[k])
            pair = comparelist[k]
            tempscore = score(k)
            initial.append(tempscore)
            
        if i > 3:                                                       ### All other loops to add to the score
            comparelist[k] = (consensus[k] + '=' + exper[k])
            pair = comparelist[k]
            tempscore = score(k)
            initial[k] = initial[k] + tempscore
            
    linetoprint = linelist[i-1]
    name = linetoprint[1:]
    basefile = os.path.realpath(os.path.join(directname,basename + '_' + str(i) + "_" + name))          ### Make a path for the file to be made in the directory given
    output = open(os.path.realpath(basefile),'w')                                           ### output for the file to be put into
    
    for k in range(0,amino-1):                  ###Loop through each amino acid and write it in tab delimited form into file
        if k == 0:
            linetoprint = linelist[i-1]
            print>>output, "Amino Acid", "\t",linetoprint[1:]               #Headers for output files of Amino Acid and whichever species was analyzed 
        print>>output, k+1,'\t', initial[k]
    
    
output = open(outputfile,'w')         ### open output file and make it writeable


### Loop through the number of amino acids and print the amino acids position, the consensus amino acid and the total score, FINAL SCORE, not new in directory 

for k in range(0,amino-1):
    if k == 0:
            print>>output, "Site Number", "\t",'Amino Acid',"\t",'Score'
    print>>output, k+1, consensus[k], initial[k]
    

    