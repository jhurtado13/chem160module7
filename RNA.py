seqs=["UUCGCCGACUGA","AUGCCUUGA","AUGCGGUGAUAA","AUGUGAGCUCCGUGA"]
for seq in seqs:
    print(seq)
    if seq.startswith("AUG"):
        print("Has start codon")
    if seq.count("UGA")>=0 and not seq.endswith("UGA"):
        print("Has selenocysteine")
    if seq.count("UGA")>1 and seq.endswith("UGA"):
        print("Has selenocystein and stop codon")
    

