#!/usr/bin/python3
def aa_content(protein, aa):
	length = len(protein)
	aa_count = protein.upper().count(aa.upper())
	aa_content = aa_count/length*100
	return aa_content

assert round(aa_content("MSRSLLLRFLLFLLLLPPLP", "M")) == round(5)
assert round(aa_content("MSRSLLLRFLLFLLLLPPLP", "r")) == round(10)
assert round(aa_content("MSRSLLLRFLLFLLLLPPLP", "L")) == round(50)
assert round(aa_content("MSRSLLLRFLLFLLLLPPLP", "Y")) == round(0)

def aa_content2(protein, aa_list="aILMFWYV"):
	length = len(protein)
	counter = 0
	for aa in aa_list:
		aa_count = protein.upper().count(aa.upper())
		counter = counter + aa_count
	percentage = counter/length*100
	return percentage

assert round(aa_content2("MSRSLLLRFLLFLLLLPPLP", ["M"])) == 5
assert round(aa_content2("MSRSLLLRFLLFLLLLPPLP", ['F', 'S', 'L'])) == 70
assert round(aa_content2("MSRSLLLRFLLFLLLLPPLP")) == 65
