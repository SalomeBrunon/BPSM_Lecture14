#!/usr/bin/python3
def dna_tresh(dna, treshold = 0.1):
	length=len(dna)
	counter = 0
	for base in ['A', 'T', 'G', 'C']:
		good_bases = dna.upper().count(base)
		counter = good_bases + counter
	fraction = counter/length
	return print(fraction >= treshold)

dna_tresh('atucgtgractanctgactg')
dna_tresh('atucgtgractanctgactg', 0.1)
dna_tresh('atucgtgractanctgactg', 0.2)
