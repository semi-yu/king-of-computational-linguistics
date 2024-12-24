"""
    Implementation; Computational language
"""
import sys
from collections import deque
# fin = sys.stdin.read().split('\n')
fin = """1
-2
X^3-X^2""".split('\n')

E = int(fin[0])

class Term:
    mult: int
    power: int

    def __init__(self, mult, power):
        self.mult = mult
        self.power = power

    def calculate(self, v): return self.mult * pow(v, self.power)

def separate(expr):
    tokens = deque([])

    last = 0
    for curr in range(len(expr)):
        if expr[curr] == '+' or expr[curr] == '-':
            term = expr[last:curr]
            last = curr

            tokens.append(term)
    tokens.append(expr[last:])

    if tokens[0] == '': # Trim useless blank
        tokens.popleft()
    
    return tokens

def lex_coef(part):
    if not part: return 1
    if len(part) == 1: 
        if part[0] == '+' or part[0] == '-': return int(part + '1')
        else: return int(part)

    return int(part)

def lex_power(part):
    if not part: return 0

    return int(part)

def lex(tokens):
    terms = deque([])

    for token in tokens:
        var_position = token.find('X')
        pow_position = token.find('^')

        coef_part = token[:var_position] if var_position != -1 else token
        power_part = token[pow_position+1:] if pow_position != -1 else ('1' if var_position != -1 else '')

        terms.append(Term(lex_coef(coef_part), lex_power(power_part)))

    return terms

for i in range(E):
    v = int(fin[2*i+1])
    expr = fin[2*i+2]

    lexes = lex(separate(expr))
    
    print(f'CASE #{i+1}: {sum([t.calculate(v) for t in lexes])}')
    