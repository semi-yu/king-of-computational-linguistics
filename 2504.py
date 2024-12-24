"""
    Implementation; Computational langauage
"""
import sys
from collections import deque
# fin = sys.stdin.read().split('\n')
fin = """[][]((])""".split('\n')

statement = fin[0]

def is_number(chr): return type(chr) is int

class Parser:
    def parse(self, statement):
        length = len(statement)

        stack = deque([])

        for i in range(length):
            chr = statement[i]

            if chr =='(' or chr == '[':
                stack.append(chr)
            elif chr == ')':
                if not stack: return 0

                top = stack.pop()

                if top == '(': 
                    stack.append(2)
                elif is_number(top):
                    res = 0

                    while is_number(top):
                        res += top
                        if not stack: return 0
                        top = stack.pop()

                    if top == '(': stack.append(2*res)                 
                    else: return 0
                else:
                    return 0
            elif chr == ']':
                if not stack: return 0

                top = stack.pop()

                if top == '[': 
                    stack.append(3)
                elif is_number(top):
                    res = 0

                    while is_number(top):
                        res += top
                        if not stack: return 0
                        top = stack.pop()

                    if top == '[': stack.append(3*res)                 
                    else: return 0
                else:
                    return 0

        ans = 0        
        for elm in stack:
            if type(elm) is int: ans += elm
            elif elm in '()[]': return 0
        
        return ans

parser = Parser()
print(parser.parse(statement))

    
