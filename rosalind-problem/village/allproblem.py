# first problem
# import this

# second problem
def hypo(a: int, b: int)-> int:
    return a**2 + b**2

# print(hypo(995, 926))


# Third problem
def stringmanu(statement: str, a: int, b: int, c: int, d: int)-> str:
    return ' '.join([statement[a:b+1], statement[c:d+1]])

# a = "FtSCJziSphenurusAuSgkGXBlN27zMcptyYZ9KRitlU29LcFXUNY3whorridumLYx2bhNISHSwZ2kEkN1gjugxa0LXjq7gzvXm2xPab1RARbQ9ZAV5L4srne1rTYRnXjTaDt8x6TLupXIEBLYIoSSjNIobYevOSkY8YWjhhAzxm44v9."
# print(stringmanu(a, 7, 15, 54, 61))


# # Forth problem
def cond(a: int, b: int)-> int:
    sum = 0
    for i in range(a, b+1):
        if i%2!=0:
            sum+=i

    return sum

# print(cond(4474, 9393))

# Fifth Problem

def manu(location: str, out: str)->None:
    with open(location, 'r') as f:
        output = [line for pos, line in enumerate(f.readlines()) if pos %2!=0]
    
    with open(out, 'w') as f:
        f.write(''.join([li for li in output]))

# manu('rosalind-problem/village/input.txt', 'rosalind-problem/village/ou.txt')


# Sixth Problem
import collections

def counting(a: str) -> None:
    temp = dict(collections.Counter(a.split(' ')))
    for i, j in temp.items():
        print(i, j)

# counting("When I find myself in times of trouble Mother Mary comes to me Speaking words of wisdom let it be And in my hour of darkness she is standing right in front of me Speaking words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the broken hearted people living in the world agree There will be an answer let it be For though they may be parted there is still a chance that they will see There will be an answer let it be Let it be let it be let it be let it be There will be an answer let it be Let it be let it be let it be let it be Whisper words of wisdom let it be Let it be let it be let it be let it be Whisper words of wisdom let it be And when the night is cloudy there is still a light that shines on me Shine until tomorrow let it be I wake up to the sound of music Mother Mary comes to me Speaking words of wisdom let it be Let it be let it be let it be yeah let it be There will be an answer let it be Let it be let it be let it be yeah let it be Whisper words of wisdom let it be")
