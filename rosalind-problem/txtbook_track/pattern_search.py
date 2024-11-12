from re import findall
def count_kmer_loop(sequence, kmer):

    return len(findall(f'(?=({kmer}))', sequence))


# Test
seq = "AATTTTAAAAC"
kmer = "AA"
print(count_kmer_loop(seq, kmer))