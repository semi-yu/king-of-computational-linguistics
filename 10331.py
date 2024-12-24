"""
    Implementation; Computational language
"""
import sys
from collections import deque
# fin = sys.stdin.read().split('\n')
fin = """1+2*3+4
11""".split('\n')

statement = fin[0]
answer = int(fin[1])

def is_number(chr):
    if chr in '0123456789': return True
    return False
    
def is_operator(chr):
    if chr in '+*': return True
    return False

def parse_number(chr): return int(chr)

def parse_operator(chr):
    return { '+': lambda a,b: a+b,
             '*': lambda a,b: a*b }[chr]
    
class FatherCalculator:
    num_stack: deque
    op_stack: deque

    def shunt(self, statement):
        self.num_stack = deque([])
        self.op_stack = deque([])

        length = len(statement)

        for idx in range(length):
            chr = statement[idx]

            if is_number(chr):
                self.num_stack.append(parse_number(chr))
            elif is_operator(chr):
                self.op_stack.append(parse_operator(chr))

    def calculate(self):
        while len(self.num_stack) >= 2:
            a = self.num_stack.popleft()
            b = self.num_stack.popleft()

            op = self.op_stack.popleft()
            self.num_stack.appendleft(op(a,b))

        return self.num_stack.pop()

class ValidCalculation:
    output: deque

    def shunt(self, statement):
        self.output = deque([])

        priority = {
            '*': 1, 
            '+': 0
        }

        length = len(statement)
        op_stack = deque([])

        for i in range(length):
            chr = statement[i]

            if is_number(chr):
                self.output.append(chr)
            elif is_operator(chr):
                if op_stack and (priority[chr] <= priority[op_stack[-1]]):
                    self.output.append(op_stack.pop())
                    op_stack.append(chr)
                else:
                    op_stack.append(chr)
        
        while op_stack:
            self.output += op_stack.pop()

        return self.output
    
    def calculate(self):
        stack = []

        while self.output:
            chr = self.output.popleft()
            
            if is_number(chr): 
                stack.append(parse_number(chr))
            elif is_operator(chr):
                a, b = stack.pop(), stack.pop()
                result = parse_operator(chr)(a,b)

                stack.append(result)

        return stack[-1]

def solve():
    global answer, statement

    father = FatherCalculator()
    valid = ValidCalculation()

    father.shunt(statement)
    valid.shunt(statement)

    father_res, valid_res = father.calculate(), valid.calculate()

    if father_res == valid_res:
        if father_res == answer: print('U')
        else: print('I')
    elif father_res == answer:
        print('L')
    elif valid_res == answer:
        print('M')
    else:
        print('I')
solve()