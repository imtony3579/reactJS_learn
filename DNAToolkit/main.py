# DNA Tool set/Code testing file
import DNAToolkit as dna
from utl import colored 
import random

radString = ''.join([random.choice(dna.Nucleotides) for _ in range(50)])

valid_seq = dna.validateSeq(radString)

print(f'\nSequence: {colored(valid_seq)}\n')
print(f'[1] + Sequence Length: {len(valid_seq)}\n')
print(colored(f'[2] + Nucleotide Frequency: {dna.countNucFrequency(valid_seq)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(dna.transcription(valid_seq))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {colored(valid_seq)} 3'")
print(f"   {''.join(['|' for _ in range(len(valid_seq))])}")
print(f"3' {colored(dna.reverse_complement(valid_seq)[::-1])} 5' [Complement]")
print(f"5' {colored(dna.reverse_complement(valid_seq))} 3' [Rev. complement] \n")

print(f'[5] + GC content: {dna.gc_content(valid_seq)}%\n')
print(f'[6] + GC content in Subsection k=5: {dna.gc_content_subset(valid_seq, k=5)}\n')

print(f'[7] + Aminoacid sequence from DNA: {dna.translate_seq(valid_seq )}\n')
print(f'[8] + Codon Frequency (L): {dna.codon_usage(valid_seq, "L")}\n')

print(f'[9] + Reading Frames:')
for i in dna.gen_reading_frame(valid_seq):
    print(i)


print(f'\n[10] + All prots in 6 open reading frames:')
for prot in dna.all_proteins_from_orfs(valid_seq,0,0,True):
    print(f'{prot}')