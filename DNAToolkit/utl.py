def colored(seq: str) -> str:

    bcolor = {
        'A': '\033[92m',
        'C': '\033[94m',
        'G': '\033[93m',
        'T': '\033[91m',
        'U': '\033[91m',
        'reset': '\033[0;0m'
    }

    tmpstr = ""

    for nuc in seq:
        if nuc in bcolor:
            tmpstr += bcolor[nuc] + nuc
        else:
            tmpstr += bcolor['reset'] + nuc
    
    return tmpstr + '\33[0;0m'