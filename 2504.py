"""
    Implementation; Computational langauge
"""
import sys
# fin = sys.stdin.read().split('\n')
fin = """(()(()))(())""".split('\n')

"""
<expr>        ::= ( <parenthesis> | <bracket> )*
<parenthesis> ::= ( '(' ( <parenthesis> | <bracket> ) ')' )* | ''
<bracket>     ::= ( '[' ( <parenthesis> | <bracket> ) ']' )* | ''
"""

class Parser:
    def parse(self):
        self.buffer = ['\0' for _ in range(30)]
        self.idx = 0

        return self.parse_expression()

    def parse_expression(self):
        result = 0
        chr = self.buffer[self.idx]

        while chr == '(' or chr == '[':
            if chr == '(':
                self.idx += 1
                result += self.parse_parenthesis()
            elif chr == ')' or chr == ']':
                raise Exception()

        return result

    def parse_parenthesis(self):
        result = 0
        chr = self.buffer[self.idx]

        if chr == '(':
            
        elif chr == ')':
            result = 2

        return result

    def parse_bracket(self):
        ...
