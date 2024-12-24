"""
    Implementation; Computational language
"""
import sys
# fin = sys.stdin.read().split('\n')
fin = """3
If the voltage is U=200V and the current is I=4.5A, which power is generated?
A light-bulb yields P=100W and the voltage is U=220V. Compute the current, please.
bla bla bla lightning strike I=2A bla bla bla P=2.5MW bla bla voltage?""".split('\n')

N = int(fin[0])
quest = []
for i in range(1,1+N):
    quest.append(fin[i])

class Parser:
    def tokenize(self, quest):
        self.tokens = quest.split(' ')

    def parse(self):
        measure = { }

        for t in self.tokens:
            if len(t) <= 1: continue
            chr = t[0]
            nxt = t[1]
            
            if self.is_datafield(chr, nxt):
                concept, value = self.parse_datafield(t)
                measure[concept] = value

        return measure
    
    def calculate(self, measure):
        result = ''

        if 'P' in measure and 'U' in measure:
            result = f"I={measure['P'] / measure['U']:.2f}" + 'A'
        elif 'P' in measure and 'I' in measure:
            result = f"U={measure['P'] / measure['I']:.2f}" + 'V'
        elif 'I' in measure and 'U' in measure:
            result = f"P={measure['I'] * measure['U']:.2f}" + 'W'

        return result

    def is_datafield(self, chr, nxt):
        if chr == 'P' or chr == 'U' or chr == 'I':
            if nxt == '=':
                return True
        return False
        
    def parse_datafield(self, token):
        concept, right = token.split('=')

        if right[-1] == '.' or right[-1] == ',': 
            right = right[:-1]

        real_number, idx = self.parse_realnumber(right)

        unit = self.parse_prefix(right[idx]) if self.is_prefix(right[idx]) else 1

        return concept, real_number * unit
        
    def parse_realnumber(self, token):
        idx = 0
        r = token[idx]
        number = ''

        while self.is_realnumber(r):
            number += r
            idx += 1
            r = token[idx]

        return float(number), idx

    def is_realnumber(self, chr):
        if chr == '0' or \
            chr == '1' or \
            chr == '2' or \
            chr == '3' or \
            chr == '4' or \
            chr == '5' or \
            chr == '6' or \
            chr == '7' or \
            chr == '8' or \
            chr == '9' or \
            chr == '.': return True
        else: return False

    def is_prefix(self, chr):
        return chr == 'm' or chr == 'k' or chr == 'M'
    
    def parse_prefix(self, chr):
        return { 'm': 0.001, 'k': 1000, 'M': 1000000 }[chr]

parse = Parser()
string = []
for q in range(N):
    parse.tokenize(quest[q])
    print(f'Problem #{q+1}\n{parse.calculate(parse.parse())}')
    if q != N-1: print()