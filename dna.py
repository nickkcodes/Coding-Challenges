def dna_to_rna(dna):
    return dna.replace("T", "U")

in_dna = "GCAT"
result = dna_to_rna(in_dna)

print(result)