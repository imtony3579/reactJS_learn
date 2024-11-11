# DNA Toolkit file 
import collections

from structures import *

# Checking the sequence to make sure it's a DNA sequence
def validateSeq(dna_seq: str):
    tmpseq = dna_seq.upper()
    for nuc in tmpseq:
        if nuc not in Nucleotides:
            return False
    return tmpseq


def countNucFrequency(valid_seq: str) -> dict:
    # tmp_freq = {'A':0, 'C': 0, 'G': 0, 'T':0}
    # for nuc in valid_seq:
    #     tmp_freq[nuc]+=1
    # return tmp_freq
    return dict(collections.Counter(valid_seq))


def transcription(seq: str)-> str:
    # DNA -> RNA Transcription
    return seq.replace("T", "U")

def reverse_complement(seq: str) -> str:
    # return ''.join([DNA_reverseComplement[letter] for letter in seq ])[::-1]
    # Other solution bit faster
    mapping = str.maketrans("ACGT", "TGCA")
    return seq.translate(mapping)[::-1]


def gc_content(seq: str) -> int:
    """GC content in DNA/RNA sequence"""
    return round((seq.count('C')+ seq.count('G'))/ len(seq) * 100) 

def gc_content_subset(seq: str, k=20 ) -> list:
    """GC content in a DNA/RNA sub-sequence length k, k=20 by default"""
    res=[]
    for i in range(0, len(seq) - k +1, k):
        subseq = seq[i:i+k]
        res.append(gc_content(subseq))
    return res

def translate_seq(seq: str, init_pos = 0) -> list:
    """Translate a DNA sequence into an aminoacid sequence"""
    return [DNA_Codons[seq[pos:pos+3]] for pos in range(init_pos, len(seq)-2, 3)]


def codon_usage(seq: str, aminoacid: str) -> dict:
    """Provide the frequency of each codon encoding a given aminoacid in a DNA sequence"""
    tmpList = []
    for i in range(0, len(seq)-2, 3):
        if DNA_Codons[seq[i:i+3]] == aminoacid:
            tmpList.append(seq[i:i+3])
    
    freqDict = dict(collections.Counter(tmpList))
    totalWeight = sum(freqDict.values())
    for seq in freqDict:
        freqDict[seq] = round(freqDict[seq]/totalWeight, 2)

    return freqDict

def gen_reading_frame(seq: str)->list:
    """Generate the six reading frames of a DNA Sequence, including the reverse complement"""
    frames = []
    frames.append(translate_seq(seq, 0))
    frames.append(translate_seq(seq, 1))
    frames.append(translate_seq(seq, 2))
    frames.append(translate_seq(reverse_complement(seq), 0))
    frames.append(translate_seq(reverse_complement(seq), 1))
    frames.append(translate_seq(reverse_complement(seq), 2))
    return frames
    
def proteins_from_rf(aa_seq: str)->list:
    """Compute all the possible proteins in an aminoacid seq and returns a list of possible proteins"""
    current_pro=[]
    proteins=[]
    for aa in aa_seq:
        if aa=='_':
            # Stop accumulating amino acid if _ -Stop was found
            if current_pro:
                for p in current_pro:
                    proteins.append(p)
                current_pro=[]
        else:
            # Start accumulating amino acid if M -Start was found
            if aa=="M":
                current_pro.append("")
            for i in range(len(current_pro)):
                current_pro[i] += aa
    return proteins

def all_proteins_from_orfs(seq: str, startReadPos=0, endReadPos=0, ordered=False) -> list:
    """Compute all the possible proteins for all the open reading frames"""
    """Protein search DB: https://www.ncbi.nlm.nih.gov/nuccore/NM_001185097.2"""
    """API can be used to pull protein info"""
    if endReadPos>startReadPos:
        rfs = gen_reading_frame(seq[startReadPos:endReadPos])
    else:
        rfs = gen_reading_frame(seq)

    res=[]
    for rf in rfs:
        prots = proteins_from_rf(rf)
        for p in prots:
            res.append(p)


    if ordered:
        return sorted(res, key=len, reverse=True)

    return res



