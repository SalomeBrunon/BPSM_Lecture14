#!/usr/bin/python3

def kmer_counting(dna, ksize=2, kminfreq=2):
	if ksize>len(dna):
		return "Sorry, your kmer length is longer than your DNA (" + str(len(dna)) +" bases)."
	if ksize<2 or ksize>50:
		return "Sorry, innapropriate kmer length, only 2 to 50 accepted here."
	kmersfound = []
	kmerstarts = list(range(0,len(dna)))
	for base in kmerstarts:
		if (base+ksize) < len(dna)+1:
			seqout=(dna)[base:base+ksize]
			kmersfound=kmersfound+[seqout]
	nrset = list(set(kmersfound))
	returnstuff = []
	for kfreqfind in nrset:
		if kmersfound.count(kfreqfind) > kminfreq:
			returnstuff.append(kfreqfind.upper()+": "+str(kmersfound.count(kfreqfind)))
	return print(returnstuff)

kmer_counting("ttagatcctgaacgtgaacgcacggatttagatcctgaacgtgaacgcacggat",2,2)
