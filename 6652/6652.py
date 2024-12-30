"""
    Implementation; Computational linguistics
"""
import sys
from collections import deque

# fin = sys.stdin.read().split('\n')
fin = """1=X
1=1+1
2=1+1
QUIT
""".split('\n')

T = len(fin)
query = []
for i in range(T):
    query.append(fin[i])

def to_arabic(roman):
    roman_tab = {
    'O': 0,
    'I': 1, 'V': 5,
    'X': 10, 'L': 50,
    'C': 100, 'D': 500,
    'M': 1000
    }

    length = len(roman)
    result, stack = 0, deque([])

    for i in range(length):
        rom = roman_tab[roman[i]]

        if stack:
            if stack[-1] < rom:
                while stack: result -= stack.pop()
                result += rom
            else:
                while stack: result += stack.pop()
                stack.append(rom)
        else:
            stack.append(rom)

    while stack: result += stack.pop()

    return result

def to_roman(arabic):
    if arabic == 0: return 'O'

    arabic_tab = {
        0: 'O',

        1: 'I', 2: 'II', 3: 'III', 4: 'IV', 5: 'V',
        6: 'VI', 7:'VII', 8: 'VIII', 9: 'IX',

        10: 'X', 20: 'XX', 30: 'XXX', 40: 'XL', 50: 'L', 
        60: 'LX', 70: 'LXX', 80: 'LXXX', 90: 'XC',

        100: 'C', 200: 'CC', 300: 'CCC', 400: 'CD', 500: 'D', 
        600: 'DC', 700: 'DCC', 800: 'DCCC', 900: 'CM',
    }

    for key in range(1000, 10001, 1000):
        arabic_tab[key] = 'M' * (key//1000)

    result, radix = '', 1

    while arabic > 0:
        digit = arabic % 10
        result = (arabic_tab[digit * radix] + result) if digit * radix != 0 else result
        
        arabic //= 10
        radix *= 10

    return result

class Calculator:
    register = [-1 for _ in range(10)]

    def execute(self, query):
        for q in query:
            if q == '': break

            if q == 'RESET':
                print('Ready')
                self.register = [-1 for _ in range(10)]
            elif q == 'QUIT':
                print('Bye')
            else:
                reg, expr = q.split('=')
                reg = int(reg)
                self.assign(reg, expr)

    def assign(self, reg, expr):
        idx = 0

        result = 0
        sign = 1

        while idx < len(expr):
            chr = expr[idx]

            if chr in '+-':
                sign = 1 if chr == '+' else -1
                idx += 1
            elif self.is_roman(chr):
                roman_buf = ''

                while self.is_roman(expr[idx]):
                    roman_buf += expr[idx]
                    idx += 1
                    if idx >= len(expr): break

                result += sign * to_arabic(roman_buf)
            elif self.is_refer(chr):
                if self.register[int(chr)] == -1:
                    print('Error')
                    return
                else:
                    result += sign * self.register[int(chr)]
                idx += 1

        if result < 0 or result > 10000:
            print('Error')
            return

        self.register[reg] = result
        print(f'{reg}={to_roman(result)}')

    def is_roman(self, chr): return chr in 'OIVXLCDM'

    def is_refer(self, chr): return chr in '0123456789'

karl = Calculator()
karl.execute(query)