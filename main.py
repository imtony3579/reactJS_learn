# DNA Tool set/Code testing file
from DNAToolkit import *
import random

radString = ''.join([random.choice(Nucleotides) for _ in range(50)])

valid_seq = validateSeq(radString)

print(countNucFrequency(valid_seq=valid_seq))

