

def gc_content(seq: str) -> int:
    """GC content in DNA/RNA sequence"""
    return round((seq.count('C')+ seq.count('G'))/ len(seq) * 100, 4) 

def computeFromFasta(filePath: str) -> dict:
    temdic = {}
    with open(filePath, 'r') as f:
        for i in f.readlines():
            i = i.strip()
            if '>' in i:
                j = i
                temdic[i]=""
            else:
                temdic[j]+=i
    
    for j,k in temdic.items():
        temdic[j]=gc_content(k)

    m = max(temdic.values())
    return {list(temdic.keys())[list(temdic.values()).index(m)], m}


print(computeFromFasta('rosalind-problem/stronghold/gcCont_fast.txt'))
