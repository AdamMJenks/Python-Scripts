#!/usr/bin/env python

f = open("rosalind_cons2.txt",'r')
all = f.readlines()[1:]

seqList = []
data = ''



for line in all:
    line = line.strip()
    if line.startswith('>'):
        final = list(data)
        seqList.append(final)
        columnnum = len(seqList[0])
        data = ''
        next
    else:
        line = line.upper()
        data = data + line

final = list(data)
seqList.append(final)


columnnum = len(seqList[0])


Aseq = [0] * columnnum
Cseq = [0] * columnnum
Gseq = [0] * columnnum
Tseq = [0] * columnnum



for x in seqList:
    for i in range(0,columnnum):
        if x[i] == "A":
            Aseq[i]= Aseq[i]+1
        elif x[i] == "C":
            Cseq[i]= Cseq[i]+1
        elif x[i] == "G":
            Gseq[i]= Gseq[i]+1
        elif x[i] == "T":
            Tseq[i]= Tseq[i]+1



Consensus = ''

for i in range (0,columnnum):
    if Aseq[i] > Cseq[i] and Aseq[i] > Gseq[i] and Aseq[i] > Tseq[i]:
        Consensus = Consensus + "A"
    if Tseq[i] > Cseq[i] and Tseq[i] > Gseq[i] and Tseq[i] > Aseq[i]:
        Consensus = Consensus + "T"
    if Cseq[i] > Tseq[i] and Cseq[i] > Gseq[i] and Cseq[i] > Aseq[i]:
        Consensus = Consensus + "C"
    if Gseq[i] > Tseq[i] and Gseq[i] > Cseq[i] and Gseq[i] > Aseq[i]:
        Consensus = Consensus + "G"

print Consensus

Adetails = ""
Cdetails = ""
Gdetails = ""
Tdetails = ""

for item in Aseq:
    Adetails += str(item)
    Adetails += ' '
    
for item in Tseq:
    Tdetails += str(item)
    Tdetails += ' '
    
for item in Cseq:
    Cdetails += str(item)
    Cdetails += ' '
    
for item in Gseq:
    Gdetails += str(item)
    Gdetails += ' '

print "A:", Adetails.strip()
print "C:", Cdetails.strip()
print "G:", Gdetails.strip()
print "T:", Tdetails.strip()


