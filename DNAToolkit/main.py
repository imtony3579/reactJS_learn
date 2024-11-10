# DNA Tool set/Code testing file
import DNAToolkit as dna
from utl import colored 
import random

radString = ''.join([random.choice(dna.Nucleotides) for _ in range(10)])

valid_seq = dna.validateSeq(radString)

print(f'\nSequence: {colored(valid_seq)}\n')
print(f'[1] + Sequence Length: {len(valid_seq)}\n')
print(colored(f'[2] + Nucleotide Frequency: {dna.countNucFrequency(valid_seq)}\n'))
print(f'[3] + DNA/RNA Transcription: {colored(dna.transcription(valid_seq))}\n')

print(f"[4] + DNA String + Reverse Complement:\n5' {colored(valid_seq)} 3'")
print(f"   {''.join(['|' for _ in range(len(valid_seq))])}")
print(f"3' {colored(dna.reverse_complement(valid_seq))} 5'\n")